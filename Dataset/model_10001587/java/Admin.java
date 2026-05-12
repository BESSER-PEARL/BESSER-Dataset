





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String Id;
    private String Name;
    private String Password;





    private Booking booking;


    public Admin(
        String Id,        String Name,        String Password    ) {
        this.Id = Id;
        this.Name = Name;
        this.Password = Password;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}