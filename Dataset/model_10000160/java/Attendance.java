





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String Name;
    private String Date___Time;
    private String Details;
    private String Position;



    public Attendance(
        String Name,        String Date___Time,        String Details,        String Position    ) {
        this.Name = Name;
        this.Date___Time = Date___Time;
        this.Details = Details;
        this.Position = Position;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDate___time() {
        return Date___Time;
    }

    public void setDate___time(String Date___Time) {
        this.Date___Time = Date___Time;
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


}