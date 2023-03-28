use chrono::{DateTime, Local};
use dotenv::dotenv;

pub fn time_now() -> DateTime<Local> {
    Local::now()
}

pub fn format_time(time: DateTime<Local>, for_export: bool) -> String {
    return if for_export {
        time.to_rfc3339().to_string()
    } else {
        time.format("%Y-%m-%d %H:%M").to_string()
    };
}

pub fn env_str(variable: &str) -> String {
    dotenv().ok();
    std::env::var(variable)
        .expect(format!("Variable {variable} must be set.").as_str())
}

pub fn env_int(variable: &str) -> u16 {
    env_str(variable)
        .parse::<u16>()
        .expect(format!("Variable {variable} must be an int.").as_str())
}

pub fn env_vec(variable: &str) -> Vec<(String, String)> {
    let env = env_str(variable);
    let mut vector: Vec<(String, String)> = Vec::new();
    for receiver in env.split(";").collect::<Vec<&str>>() {
        let split = receiver.split(",").collect::<Vec<&str>>();
        vector.push((String::from(split[0]), String::from(split[1])));
    }

    vector
}
