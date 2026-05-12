





import java.util.List;
import java.util.ArrayList;

public class Guest  {

    private String Name;
    private String Phone;
    private String Guest_ID;



    public Guest(
        String Name,        String Phone,        String Guest_ID    ) {
        this.Name = Name;
        this.Phone = Phone;
        this.Guest_ID = Guest_ID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getGuest_id() {
        return Guest_ID;
    }

    public void setGuest_id(String Guest_ID) {
        this.Guest_ID = Guest_ID;
    }


}