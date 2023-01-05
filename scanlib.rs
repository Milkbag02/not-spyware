use std::fs;
use std::path::Path;

#[pyfunction]
fn scan_directory(path: &str) -> Vec<String> {
    let mut entries = Vec::new();
    for entry in fs::read_dir(Path::new(path)).unwrap() {
        let entry = entry.unwrap();
        entries.push(entry.path().to_str().unwrap().to_owned());
    }
    entries
}

