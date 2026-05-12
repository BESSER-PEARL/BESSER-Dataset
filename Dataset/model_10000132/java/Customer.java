





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Name;
    private String DOB;
    private int Card_num;
    private int Pin;



    public Customer(
        String Name,        String DOB,        int Card_num,        int Pin    ) {
        this.Name = Name;
        this.DOB = DOB;
        this.Card_num = Card_num;
        this.Pin = Pin;
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


}