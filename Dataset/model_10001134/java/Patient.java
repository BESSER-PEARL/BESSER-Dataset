





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private None employee;
    private String patientid;
    private String ICD;
    private float approvedHours;





    private account account;


    public Patient(
        None employee,        String patientid,        String ICD,        float approvedHours    ) {
        this.employee = employee;
        this.patientid = patientid;
        this.ICD = ICD;
        this.approvedHours = approvedHours;
    }


    public None getEmployee() {
        return employee;
    }

    public void setEmployee(None employee) {
        this.employee = employee;
    }
    public String getPatientid() {
        return patientid;
    }

    public void setPatientid(String patientid) {
        this.patientid = patientid;
    }
    public String getIcd() {
        return ICD;
    }

    public void setIcd(String ICD) {
        this.ICD = ICD;
    }
    public float getApprovedhours() {
        return approvedHours;
    }

    public void setApprovedhours(float approvedHours) {
        this.approvedHours = approvedHours;
    }

    public account getAccount() {
        return account;
    }

    public void setAccount(account account) {
        this.account = account;
    }

}