





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String Name;
    private String Position;
    private String Details;
    private String Date___Time;



    public Attendance(
        String Name,        String Position,        String Details,        String Date___Time    ) {
        this.Name = Name;
        this.Position = Position;
        this.Details = Details;
        this.Date___Time = Date___Time;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPosition() {
        return Position;
    }

    public void setPosition(String Position) {
        this.Position = Position;
    }
    public String getDetails() {
        return Details;
    }

    public void setDetails(String Details) {
        this.Details = Details;
    }
    public String getDate___time() {
        return Date___Time;
    }

    public void setDate___time(String Date___Time) {
        this.Date___Time = Date___Time;
    }


}