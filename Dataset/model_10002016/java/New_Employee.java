





import java.util.List;
import java.util.ArrayList;

public class New_Employee  {

    private String Place_of_Birth;
    private String Date_of_Birth;
    private String Position;
    private String Division;
    private String Name;
    private String Working_Since;





    private Task task;




    private Registration registration;




    private Attendance attendance;


    public New_Employee(
        String Place_of_Birth,        String Date_of_Birth,        String Position,        String Division,        String Name,        String Working_Since    ) {
        this.Place_of_Birth = Place_of_Birth;
        this.Date_of_Birth = Date_of_Birth;
        this.Position = Position;
        this.Division = Division;
        this.Name = Name;
        this.Working_Since = Working_Since;
    }


    public String getPlace_of_birth() {
        return Place_of_Birth;
    }

    public void setPlace_of_birth(String Place_of_Birth) {
        this.Place_of_Birth = Place_of_Birth;
    }
    public String getDate_of_birth() {
        return Date_of_Birth;
    }

    public void setDate_of_birth(String Date_of_Birth) {
        this.Date_of_Birth = Date_of_Birth;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getDivision() {
        return Division;
    }

    public void setDivision(String Division) {
        this.Division = Division;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getWorking_since() {
        return Working_Since;
    }

    public void setWorking_since(String Working_Since) {
        this.Working_Since = Working_Since;
    }

    public Task getTask() {
        return task;
    }

    public void setTask(Task task) {
        this.task = task;
    }
    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }
    public Attendance getAttendance() {
        return attendance;
    }

    public void setAttendance(Attendance attendance) {
        this.attendance = attendance;
    }

}