





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String dob;
    private String name;
    private int pin;
    private int cardnumber;
    private String address;





    private Account account;


    public Customer(
        String dob,        String name,        int pin,        int cardnumber,        String address    ) {
        this.dob = dob;
        this.name = name;
        this.pin = pin;
        this.cardnumber = cardnumber;
        this.address = address;
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
    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }
    public int getCardnumber() {
        return cardnumber;
    }

    public void setCardnumber(int cardnumber) {
        this.cardnumber = cardnumber;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}