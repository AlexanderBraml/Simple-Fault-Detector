use std::fs;
use std::net::UdpSocket;

use chrono::{DateTime, Duration, Local};

use crate::mailer::send_mail;
use crate::utils::{env_int, env_str, format_time, time_now};

static ALARM_FILE: &str = "alarm.txt";

pub fn time_for_alarm(last: DateTime<Local>) -> bool {
    time_now() >= last + Duration::minutes(i64::from(env_int("ALARM_PAUSE_MINUTES")))
}

fn alarm(time: DateTime<Local>) {
    println!("ALARM at {}! Sending e-mails...", format_time(time, false));

    tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .build()
        .unwrap()
        .block_on(send_mail());

    println!("Done sending e-mails.");
}

fn import_alarm() -> DateTime<Local> {
    return if let Ok(time) = fs::read_to_string(ALARM_FILE) {
        if let Ok(parsed) = DateTime::parse_from_rfc3339(&time) {
            DateTime::from(parsed)
        } else {
            time_now() - Duration::minutes(i64::from(env_int("ALARM_PAUSE_MINUTES")))
        }
    } else {
        time_now() - Duration::minutes(i64::from(env_int("ALARM_PAUSE_MINUTES")))
    };
}

fn export_alarm(alarm: DateTime<Local>) {
    fs::write(ALARM_FILE, format_time(alarm, true))
        .expect("Could not write to file.");
}

pub fn listen_for_alarm() {
    let socket = UdpSocket::bind(env_str("CLIENT"))
        .expect("Could not bind socket to ip and port.");

    let mut last_alarm = import_alarm();

    loop {
        let mut buf = [0; 10];
        let (amt, _) = socket.recv_from(&mut buf)
            .expect("Receiving message from socket failed.");
        let dec = std::str::from_utf8(&buf[..amt])
            .expect("Invalid UTF-8 sequence.");

        if dec == "1" && time_for_alarm(last_alarm) {
            last_alarm = time_now();
            alarm(last_alarm);
            export_alarm(last_alarm);
        } else {
            println!("Alarm already triggered.");
        }
    }
}
