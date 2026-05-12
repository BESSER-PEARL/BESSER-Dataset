





import java.util.List;
import java.util.ArrayList;

public class BloodBank  {

    private String bloodGroup;
    private String phone;





    private Hospital hospital;


    public BloodBank(
        String bloodGroup,        String phone    ) {
        this.bloodGroup = bloodGroup;
        this.phone = phone;
    }


    public String getBloodgroup() {
        return bloodGroup;
    }

    public void setBloodgroup(String bloodGroup) {
        this.bloodGroup = bloodGroup;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

}