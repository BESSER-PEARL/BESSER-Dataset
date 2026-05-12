





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int cardno;
    private String dob;
    private String name;
    private String address;
    private int pin;



    public Customer(
        int cardno,        String dob,        String name,        String address,        int pin    ) {
        this.cardno = cardno;
        this.dob = dob;
        this.name = name;
        this.address = address;
        this.pin = pin;
    }


    public int getCardno() {
        return cardno;
    }

    public void setCardno(int cardno) {
        this.cardno = cardno;
    }
    public String getDob() {
        return dob;
    }

    public void setDob(String dob) {
        this.dob = dob;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }


}