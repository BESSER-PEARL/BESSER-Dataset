





import java.util.List;
import java.util.ArrayList;

public class patient  {

    private int Patient_Contact_NO;
    private String Status;
    private String DOB;
    private String Sex;
    private String Patient_Address;
    private int Patient_ID;
    private String Patient_Name;





    private List<Doctor> doctors;


    public patient(
        int Patient_Contact_NO,        String Status,        String DOB,        String Sex,        String Patient_Address,        int Patient_ID,        String Patient_Name    ) {
        this.Patient_Contact_NO = Patient_Contact_NO;
        this.Status = Status;
        this.DOB = DOB;
        this.Sex = Sex;
        this.Patient_Address = Patient_Address;
        this.Patient_ID = Patient_ID;
        this.Patient_Name = Patient_Name;
        this.doctors = new ArrayList<>();
    }

    public patient(
        int Patient_Contact_NO,        String Status,        String DOB,        String Sex,        String Patient_Address,        int Patient_ID,        String Patient_Name        ArrayList<Doctor> doctors    ) {
        this.Patient_Contact_NO = Patient_Contact_NO;
        this.Status = Status;
        this.DOB = DOB;
        this.Sex = Sex;
        this.Patient_Address = Patient_Address;
        this.Patient_ID = Patient_ID;
        this.Patient_Name = Patient_Name;
        this.doctors = doctors;
    }

    public int getPatient_contact_no() {
        return Patient_Contact_NO;
    }

    public void setPatient_contact_no(int Patient_Contact_NO) {
        this.Patient_Contact_NO = Patient_Contact_NO;
    }
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }
    public String getSex() {
        return Sex;
    }

    public void setSex(String Sex) {
        this.Sex = Sex;
    }
    public String getPatient_address() {
        return Patient_Address;
    }

    public void setPatient_address(String Patient_Address) {
        this.Patient_Address = Patient_Address;
    }
    public int getPatient_id() {
        return Patient_ID;
    }

    public void setPatient_id(int Patient_ID) {
        this.Patient_ID = Patient_ID;
    }
    public String getPatient_name() {
        return Patient_Name;
    }

    public void setPatient_name(String Patient_Name) {
        this.Patient_Name = Patient_Name;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}