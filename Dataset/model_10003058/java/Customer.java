





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Location;
    private String Fullname;
    private int Card_details;
    private String Gender;



    public Customer(
        String Location,        String Fullname,        int Card_details,        String Gender    ) {
        this.Location = Location;
        this.Fullname = Fullname;
        this.Card_details = Card_details;
        this.Gender = Gender;
    }


    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }
    public String getFullname() {
        return Fullname;
    }

    public void setFullname(String Fullname) {
        this.Fullname = Fullname;
    }
    public int getCard_details() {
        return Card_details;
    }

    public void setCard_details(int Card_details) {
        this.Card_details = Card_details;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }


}