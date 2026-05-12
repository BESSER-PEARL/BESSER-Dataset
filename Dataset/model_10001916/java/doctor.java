





import java.util.List;
import java.util.ArrayList;

public class doctor  {

    private None salary;
    private String doctor_name;
    private boolean attendance;
    private None doctor_id;





    private patient patient;


    public doctor(
        None salary,        String doctor_name,        boolean attendance,        None doctor_id    ) {
        this.salary = salary;
        this.doctor_name = doctor_name;
        this.attendance = attendance;
        this.doctor_id = doctor_id;
    }


    public None getSalary() {
        return salary;
    }

    public void setSalary(None salary) {
        this.salary = salary;
    }
    public String getDoctor_name() {
        return doctor_name;
    }

    public void setDoctor_name(String doctor_name) {
        this.doctor_name = doctor_name;
    }
    public boolean getAttendance() {
        return attendance;
    }

    public void setAttendance(boolean attendance) {
        this.attendance = attendance;
    }
    public None getDoctor_id() {
        return doctor_id;
    }

    public void setDoctor_id(None doctor_id) {
        this.doctor_id = doctor_id;
    }

    public patient getPatient() {
        return patient;
    }

    public void setPatient(patient patient) {
        this.patient = patient;
    }

}