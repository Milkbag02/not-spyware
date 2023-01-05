use pyo3::prelude::*;

#[pymodule]
fn directory_scanner(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(scan_directory))?;
    Ok(())
}
