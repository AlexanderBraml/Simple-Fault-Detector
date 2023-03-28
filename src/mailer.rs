use mail_send::mail_builder::MessageBuilder;
use mail_send::SmtpClientBuilder;

use crate::utils::{env_int, env_str, env_vec, format_time, time_now};

pub async fn send_mail() {
    let from = env_vec("ALARM_MESSAGE_FROM");
    let from = from.get(0)
        .expect("You have to specify the sender of the message correctly.");

    let message = MessageBuilder::new()
        .from((from.0.as_str(), from.1.as_str()))
        .to(env_vec("EMAIL_RECEIVERS"))
        .subject(env_str("ALARM_MESSAGE_SUBJECT"))
        .html_body(env_str("ALARM_MESSAGE_BODY")
            .replace("{datetime}", format_time(time_now(), false).as_str()));

    SmtpClientBuilder::new(env_str("SMTP_SERVER"), env_int("SMTP_PORT"))
        .implicit_tls(true)
        .credentials((env_str("EMAIL_SENDER"), env_str("EMAIL_PASSWORD")))
        .connect()
        .await
        .expect("Could not connect to server.")
        .send(message)
        .await
        .expect("Could not send message.");
}
