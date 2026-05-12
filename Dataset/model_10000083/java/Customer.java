





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int Pin;
    private int Card_num;
    private String Name;
    private String DOB;



    public Customer(
        int Pin,        int Card_num,        String Name,        String DOB    ) {
        this.Pin = Pin;
        this.Card_num = Card_num;
        this.Name = Name;
        this.DOB = DOB;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }


}