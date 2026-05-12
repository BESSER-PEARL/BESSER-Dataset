





import java.util.List;
import java.util.ArrayList;

public class admin  {

    private String Experience;





    private Staff staff;


    public admin(
        String Experience    ) {
        this.Experience = Experience;
    }


    public String getExperience() {
        return Experience;
    }

    public void setExperience(String Experience) {
        this.Experience = Experience;
    }

    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }

}