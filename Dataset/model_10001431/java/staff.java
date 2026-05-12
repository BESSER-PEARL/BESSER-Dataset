





import java.util.List;
import java.util.ArrayList;

public class staff  {

    private String name;
    private int staffID;
    private String jobtype;





    private restaurant restaurant;


    public staff(
        String name,        int staffID,        String jobtype    ) {
        this.name = name;
        this.staffID = staffID;
        this.jobtype = jobtype;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getStaffid() {
        return staffID;
    }

    public void setStaffid(int staffID) {
        this.staffID = staffID;
    }
    public String getJobtype() {
        return jobtype;
    }

    public void setJobtype(String jobtype) {
        this.jobtype = jobtype;
    }

    public restaurant getRestaurant() {
        return restaurant;
    }

    public void setRestaurant(restaurant restaurant) {
        this.restaurant = restaurant;
    }

}