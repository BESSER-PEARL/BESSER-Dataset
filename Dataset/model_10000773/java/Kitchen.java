





import java.util.List;
import java.util.ArrayList;

public class Kitchen  {

    private String TimeID;





    private System system;




    private Start_Of_Day start_of_day;




    private End_Of_Day end_of_day;


    public Kitchen(
        String TimeID    ) {
        this.TimeID = TimeID;
    }


    public String getTimeid() {
        return TimeID;
    }

    public void setTimeid(String TimeID) {
        this.TimeID = TimeID;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }
    public Start_Of_Day getStart_of_day() {
        return start_of_day;
    }

    public void setStart_of_day(Start_Of_Day start_of_day) {
        this.start_of_day = start_of_day;
    }
    public End_Of_Day getEnd_of_day() {
        return end_of_day;
    }

    public void setEnd_of_day(End_Of_Day end_of_day) {
        this.end_of_day = end_of_day;
    }

}