





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String Staff_ID;
    private String Name;
    private String JobType;
    private String Phone;



    public Staff(
        String Staff_ID,        String Name,        String JobType,        String Phone    ) {
        this.Staff_ID = Staff_ID;
        this.Name = Name;
        this.JobType = JobType;
        this.Phone = Phone;
    }


    public String getStaff_id() {
        return Staff_ID;
    }

    public void setStaff_id(String Staff_ID) {
        this.Staff_ID = Staff_ID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getJobtype() {
        return JobType;
    }

    public void setJobtype(String JobType) {
        this.JobType = JobType;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }


}