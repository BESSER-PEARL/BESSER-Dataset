





import java.util.List;
import java.util.ArrayList;

public class New_Employee  {

    private String Position;
    private String Place_of_Birth;
    private String Name;
    private String Working_Since;
    private String Date_of_Birth;
    private String Division;





    private Task task;


    public New_Employee(
        String Position,        String Place_of_Birth,        String Name,        String Working_Since,        String Date_of_Birth,        String Division    ) {
        this.Position = Position;
        this.Place_of_Birth = Place_of_Birth;
        this.Name = Name;
        this.Working_Since = Working_Since;
        this.Date_of_Birth = Date_of_Birth;
        this.Division = Division;
    }


    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getPlace_of_birth() {
        return Place_of_Birth;
    }

    public void setPlace_of_birth(String Place_of_Birth) {
        this.Place_of_Birth = Place_of_Birth;
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
    public String getDate_of_birth() {
        return Date_of_Birth;
    }

    public void setDate_of_birth(String Date_of_Birth) {
        this.Date_of_Birth = Date_of_Birth;
    }
    public String getDivision() {
        return Division;
    }

    public void setDivision(String Division) {
        this.Division = Division;
    }

    public Task getTask() {
        return task;
    }

    public void setTask(Task task) {
        this.task = task;
    }

}