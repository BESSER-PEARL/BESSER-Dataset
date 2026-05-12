





import java.util.List;
import java.util.ArrayList;

public class Member  {

    private int Mobile_number;
    private String Email_address;
    private String L_name;
    private String Scientific_qualifications;
    private String F_name;
    private String Vacation_type;
    private String Job;



    public Member(
        int Mobile_number,        String Email_address,        String L_name,        String Scientific_qualifications,        String F_name,        String Vacation_type,        String Job    ) {
        this.Mobile_number = Mobile_number;
        this.Email_address = Email_address;
        this.L_name = L_name;
        this.Scientific_qualifications = Scientific_qualifications;
        this.F_name = F_name;
        this.Vacation_type = Vacation_type;
        this.Job = Job;
    }


    public int getMobile_number() {
        return Mobile_number;
    }

    public void setMobile_number(int Mobile_number) {
        this.Mobile_number = Mobile_number;
    }
    public String getEmail_address() {
        return Email_address;
    }

    public void setEmail_address(String Email_address) {
        this.Email_address = Email_address;
    }
    public String getL_name() {
        return L_name;
    }

    public void setL_name(String L_name) {
        this.L_name = L_name;
    }
    public String getScientific_qualifications() {
        return Scientific_qualifications;
    }

    public void setScientific_qualifications(String Scientific_qualifications) {
        this.Scientific_qualifications = Scientific_qualifications;
    }
    public String getF_name() {
        return F_name;
    }

    public void setF_name(String F_name) {
        this.F_name = F_name;
    }
    public String getVacation_type() {
        return Vacation_type;
    }

    public void setVacation_type(String Vacation_type) {
        this.Vacation_type = Vacation_type;
    }
    public String getJob() {
        return Job;
    }

    public void setJob(String Job) {
        this.Job = Job;
    }


}