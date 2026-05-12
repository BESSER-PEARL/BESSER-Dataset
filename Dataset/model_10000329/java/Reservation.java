





import java.util.List;
import java.util.ArrayList;

public class Reservation  {

    private String ReservationID;
    private None Date;
    private String Time;





    private Host host;


    public Reservation(
        String ReservationID,        None Date,        String Time    ) {
        this.ReservationID = ReservationID;
        this.Date = Date;
        this.Time = Time;
    }


    public String getReservationid() {
        return ReservationID;
    }

    public void setReservationid(String ReservationID) {
        this.ReservationID = ReservationID;
    }
    public None getDate() {
        return Date;
    }

    public void setDate(None Date) {
        this.Date = Date;
    }
    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }

    public Host getHost() {
        return host;
    }

    public void setHost(Host host) {
        this.host = host;
    }

}