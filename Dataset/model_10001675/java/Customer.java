





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String card_number;
    private String pin;
    private String dob;
    private String name;
    private String address;



    public Customer(
        String card_number,        String pin,        String dob,        String name,        String address    ) {
        this.card_number = card_number;
        this.pin = pin;
        this.dob = dob;
        this.name = name;
        this.address = address;
    }


    public String getCard_number() {
        return card_number;
    }

    public void setCard_number(String card_number) {
        this.card_number = card_number;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
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


}