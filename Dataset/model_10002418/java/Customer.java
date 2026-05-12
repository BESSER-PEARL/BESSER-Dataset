





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int Card_number;
    private String Date_of_birth;
    private int Pin;
    private String Name;



    public Customer(
        int Card_number,        String Date_of_birth,        int Pin,        String Name    ) {
        this.Card_number = Card_number;
        this.Date_of_birth = Date_of_birth;
        this.Pin = Pin;
        this.Name = Name;
    }


    public int getCard_number() {
        return Card_number;
    }

    public void setCard_number(int Card_number) {
        this.Card_number = Card_number;
    }
    public String getDate_of_birth() {
        return Date_of_birth;
    }

    public void setDate_of_birth(String Date_of_birth) {
        this.Date_of_birth = Date_of_birth;
    }
    public int getPin() {
        return Pin;
    }

    public void setPin(int Pin) {
        this.Pin = Pin;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}