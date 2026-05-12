





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String DOB;
    private int Pin;
    private String Name;
    private int Card_num;



    public Customer(
        String DOB,        int Pin,        String Name,        int Card_num    ) {
        this.DOB = DOB;
        this.Pin = Pin;
        this.Name = Name;
        this.Card_num = Card_num;
    }


    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
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
    public int getCard_num() {
        return Card_num;
    }

    public void setCard_num(int Card_num) {
        this.Card_num = Card_num;
    }


}