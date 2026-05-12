





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int Card_num;
    private int Pin;
    private String DOB;
    private String Name;



    public Customer(
        int Card_num,        int Pin,        String DOB,        String Name    ) {
        this.Card_num = Card_num;
        this.Pin = Pin;
        this.DOB = DOB;
        this.Name = Name;
    }


    public int getCard_num() {
        return Card_num;
    }

    public void setCard_num(int Card_num) {
        this.Card_num = Card_num;
    }
    public int getPin() {
        return Pin;
    }

    public void setPin(int Pin) {
        this.Pin = Pin;
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


}