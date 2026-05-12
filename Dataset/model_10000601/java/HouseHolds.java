





import java.util.List;
import java.util.ArrayList;

public class HouseHolds  {

    private String Computer;
    private String Light;
    private String Fan;
    private String TimeID;





    private Start_Of_Day start_of_day;




    private End_Of_Day end_of_day;


    public HouseHolds(
        String Computer,        String Light,        String Fan,        String TimeID    ) {
        this.Computer = Computer;
        this.Light = Light;
        this.Fan = Fan;
        this.TimeID = TimeID;
    }


    public String getComputer() {
        return Computer;
    }

    public void setComputer(String Computer) {
        this.Computer = Computer;
    }
    public String getLight() {
        return Light;
    }

    public void setLight(String Light) {
        this.Light = Light;
    }
    public String getFan() {
        return Fan;
    }

    public void setFan(String Fan) {
        this.Fan = Fan;
    }
    public String getTimeid() {
        return TimeID;
    }

    public void setTimeid(String TimeID) {
        this.TimeID = TimeID;
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