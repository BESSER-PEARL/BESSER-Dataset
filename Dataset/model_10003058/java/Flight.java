





import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private String Source;
    private String Name;
    private int Time;
    private None Id;
    private String Destination;
    private int Number_of_seats;



    public Flight(
        String Source,        String Name,        int Time,        None Id,        String Destination,        int Number_of_seats    ) {
        this.Source = Source;
        this.Name = Name;
        this.Time = Time;
        this.Id = Id;
        this.Destination = Destination;
        this.Number_of_seats = Number_of_seats;
    }


    public String getSource() {
        return Source;
    }

    public void setSource(String Source) {
        this.Source = Source;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getTime() {
        return Time;
    }

    public void setTime(int Time) {
        this.Time = Time;
    }
    public None getId() {
        return Id;
    }

    public void setId(None Id) {
        this.Id = Id;
    }
    public String getDestination() {
        return Destination;
    }

    public void setDestination(String Destination) {
        this.Destination = Destination;
    }
    public int getNumber_of_seats() {
        return Number_of_seats;
    }

    public void setNumber_of_seats(int Number_of_seats) {
        this.Number_of_seats = Number_of_seats;
    }


}