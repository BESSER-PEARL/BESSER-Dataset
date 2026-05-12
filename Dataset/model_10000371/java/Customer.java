





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String DOB;
    private String Name;
    private int Pin;
    private int Card_num;



    public Customer(
        String DOB,        String Name,        int Pin,        int Card_num    ) {
        this.DOB = DOB;
        this.Name = Name;
        this.Pin = Pin;
        this.Card_num = Card_num;
    }


    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getPin() {
        return Pin;
    }

    public void setPin(int Pin) {
        this.Pin = Pin;
    }
    public int getCard_num() {
        return Card_num;
    }

    public void setCard_num(int Card_num) {
        this.Card_num = Card_num;
    }


}