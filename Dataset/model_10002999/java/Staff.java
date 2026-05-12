





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private int jobType;
    private String staff_Id;
    private String contact;
    private String name;



    public Staff(
        int jobType,        String staff_Id,        String contact,        String name    ) {
        this.jobType = jobType;
        this.staff_Id = staff_Id;
        this.contact = contact;
        this.name = name;
    }


    public int getJobtype() {
        return jobType;
    }

    public void setJobtype(int jobType) {
        this.jobType = jobType;
    }
    public String getStaff_id() {
        return staff_Id;
    }

    public void setStaff_id(String staff_Id) {
        this.staff_Id = staff_Id;
    }
    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}