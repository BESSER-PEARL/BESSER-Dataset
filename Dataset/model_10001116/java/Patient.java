





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int PatientId;
    private int age;
    private String Name;





    private Doctor doctor;


    public Patient(
        int PatientId,        int age,        String Name    ) {
        this.PatientId = PatientId;
        this.age = age;
        this.Name = Name;
    }


    public int getPatientid() {
        return PatientId;
    }

    public void setPatientid(int PatientId) {
        this.PatientId = PatientId;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}