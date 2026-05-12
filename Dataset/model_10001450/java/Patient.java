





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String patientSurname;
    private float coupon;
    private String patientName;
    private int patientID;
    private String patientEmail;
    private String patientAddress;
    private String patientMobile;



    public Patient(
        String patientSurname,        float coupon,        String patientName,        int patientID,        String patientEmail,        String patientAddress,        String patientMobile    ) {
        this.patientSurname = patientSurname;
        this.coupon = coupon;
        this.patientName = patientName;
        this.patientID = patientID;
        this.patientEmail = patientEmail;
        this.patientAddress = patientAddress;
        this.patientMobile = patientMobile;
    }


    public String getPatientsurname() {
        return patientSurname;
    }

    public void setPatientsurname(String patientSurname) {
        this.patientSurname = patientSurname;
    }
    public float getCoupon() {
        return coupon;
    }

    public void setCoupon(float coupon) {
        this.coupon = coupon;
    }
    public String getPatientname() {
        return patientName;
    }

    public void setPatientname(String patientName) {
        this.patientName = patientName;
    }
    public int getPatientid() {
        return patientID;
    }

    public void setPatientid(int patientID) {
        this.patientID = patientID;
    }
    public String getPatientemail() {
        return patientEmail;
    }

    public void setPatientemail(String patientEmail) {
        this.patientEmail = patientEmail;
    }
    public String getPatientaddress() {
        return patientAddress;
    }

    public void setPatientaddress(String patientAddress) {
        this.patientAddress = patientAddress;
    }
    public String getPatientmobile() {
        return patientMobile;
    }

    public void setPatientmobile(String patientMobile) {
        this.patientMobile = patientMobile;
    }


}