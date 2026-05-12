





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String Name;
    private String Details;
    private String Position;
    private String Date___Time;





    private New_Employee new_employee;




    private Assessment assessment;


    public Attendance(
        String Name,        String Details,        String Position,        String Date___Time    ) {
        this.Name = Name;
        this.Details = Details;
        this.Position = Position;
        this.Date___Time = Date___Time;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDetails() {
        return Details;
    }

    public void setDetails(String Details) {
        this.Details = Details;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getDate___time() {
        return Date___Time;
    }

    public void setDate___time(String Date___Time) {
        this.Date___Time = Date___Time;
    }

    public New_Employee getNew_employee() {
        return new_employee;
    }

    public void setNew_employee(New_Employee new_employee) {
        this.new_employee = new_employee;
    }
    public Assessment getAssessment() {
        return assessment;
    }

    public void setAssessment(Assessment assessment) {
        this.assessment = assessment;
    }

}