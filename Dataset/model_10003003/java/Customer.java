





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String DOB;
    private int Card_num;
    private String Name;
    private int Pin;



    public Customer(
        String DOB,        int Card_num,        String Name,        int Pin    ) {
        this.DOB = DOB;
        this.Card_num = Card_num;
        this.Name = Name;
        this.Pin = Pin;
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


}