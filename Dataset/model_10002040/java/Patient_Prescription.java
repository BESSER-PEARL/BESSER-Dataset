





import java.util.List;
import java.util.ArrayList;

public class Patient_Prescription  {

    private int code;
    private int code1;
    private int diseaseid;
    private int patientid;
    private String date;
    private int medicineid;





    private Patient patient;




    private Disease disease;


    public Patient_Prescription(
        int code,        int code1,        int diseaseid,        int patientid,        String date,        int medicineid    ) {
        this.code = code;
        this.code1 = code1;
        this.diseaseid = diseaseid;
        this.patientid = patientid;
        this.date = date;
        this.medicineid = medicineid;
    }


    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }
    public int getCode1() {
        return code1;
    }

    public void setCode1(int code1) {
        this.code1 = code1;
    }
    public int getDiseaseid() {
        return diseaseid;
    }

    public void setDiseaseid(int diseaseid) {
        this.diseaseid = diseaseid;
    }
    public int getPatientid() {
        return patientid;
    }

    public void setPatientid(int patientid) {
        this.patientid = patientid;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getMedicineid() {
        return medicineid;
    }

    public void setMedicineid(int medicineid) {
        this.medicineid = medicineid;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public Disease getDisease() {
        return disease;
    }

    public void setDisease(Disease disease) {
        this.disease = disease;
    }

}