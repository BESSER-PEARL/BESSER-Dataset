





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String name;
    private int jobType;
    private String contact;
    private String staff_Id;



    public Staff(
        String name,        int jobType,        String contact,        String staff_Id    ) {
        this.name = name;
        this.jobType = jobType;
        this.contact = contact;
        this.staff_Id = staff_Id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getJobtype() {
        return jobType;
    }

    public void setJobtype(int jobType) {
        this.jobType = jobType;
    }
    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public String getStaff_id() {
        return staff_Id;
    }

    public void setStaff_id(String staff_Id) {
        this.staff_Id = staff_Id;
    }


}