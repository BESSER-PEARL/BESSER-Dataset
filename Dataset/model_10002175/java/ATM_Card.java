





import java.util.List;
import java.util.ArrayList;

public class ATM_Card  {

    private String pin;
    private String cardNumber;



    public ATM_Card(
        String pin,        String cardNumber    ) {
        this.pin = pin;
        this.cardNumber = cardNumber;
    }


    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }
    public String getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }


}