





import java.util.List;
import java.util.ArrayList;

public class Beneficiary  {

    private String Marital_status;
    private String Job;
    private int Beneficiary__ID;
    private int House_number;
    private String L_name;
    private String Date_of_birth;
    private String Address;
    private int Phone;
    private String F_name;
    private String Scientific_qualification;
    private String District;



    public Beneficiary(
        String Marital_status,        String Job,        int Beneficiary__ID,        int House_number,        String L_name,        String Date_of_birth,        String Address,        int Phone,        String F_name,        String Scientific_qualification,        String District    ) {
        this.Marital_status = Marital_status;
        this.Job = Job;
        this.Beneficiary__ID = Beneficiary__ID;
        this.House_number = House_number;
        this.L_name = L_name;
        this.Date_of_birth = Date_of_birth;
        this.Address = Address;
        this.Phone = Phone;
        this.F_name = F_name;
        this.Scientific_qualification = Scientific_qualification;
        this.District = District;
    }


    public String getMarital_status() {
        return Marital_status;
    }

    public void setMarital_status(String Marital_status) {
        this.Marital_status = Marital_status;
    }
    public String getJob() {
        return Job;
    }

    public void setJob(String Job) {
        this.Job = Job;
    }
    public int getBeneficiary__id() {
        return Beneficiary__ID;
    }

    public void setBeneficiary__id(int Beneficiary__ID) {
        this.Beneficiary__ID = Beneficiary__ID;
    }
    public int getHouse_number() {
        return House_number;
    }

    public void setHouse_number(int House_number) {
        this.House_number = House_number;
    }
    public String getL_name() {
        return L_name;
    }

    public void setL_name(String L_name) {
        this.L_name = L_name;
    }
    public String getDate_of_birth() {
        return Date_of_birth;
    }

    public void setDate_of_birth(String Date_of_birth) {
        this.Date_of_birth = Date_of_birth;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public String getF_name() {
        return F_name;
    }

    public void setF_name(String F_name) {
        this.F_name = F_name;
    }
    public String getScientific_qualification() {
        return Scientific_qualification;
    }

    public void setScientific_qualification(String Scientific_qualification) {
        this.Scientific_qualification = Scientific_qualification;
    }
    public String getDistrict() {
        return District;
    }

    public void setDistrict(String District) {
        this.District = District;
    }


}