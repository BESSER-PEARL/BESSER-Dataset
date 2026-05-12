





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String contact;
    private int jobType;
    private String name;
    private String staff_Id;



    public Staff(
        String contact,        int jobType,        String name,        String staff_Id    ) {
        this.contact = contact;
        this.jobType = jobType;
        this.name = name;
        this.staff_Id = staff_Id;
    }


    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public int getJobtype() {
        return jobType;
    }

    public void setJobtype(int jobType) {
        this.jobType = jobType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStaff_id() {
        return staff_Id;
    }

    public void setStaff_id(String staff_Id) {
        this.staff_Id = staff_Id;
    }


}