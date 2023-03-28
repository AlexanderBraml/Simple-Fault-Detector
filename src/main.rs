use crate::receiver::listen_for_alarm;

mod receiver;
mod mailer;
mod utils;

fn main() {
    listen_for_alarm();
}
