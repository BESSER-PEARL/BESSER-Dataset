





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String card_type;
    private int amount;
    private int password;
    private int cvv;
    private int card_no;





    private Guest guest;




    private Manager manager;


    public Payment(
        String card_type,        int amount,        int password,        int cvv,        int card_no    ) {
        this.card_type = card_type;
        this.amount = amount;
        this.password = password;
        this.cvv = cvv;
        this.card_no = card_no;
    }


    public String getCard_type() {
        return card_type;
    }

    public void setCard_type(String card_type) {
        this.card_type = card_type;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }
    public int getCvv() {
        return cvv;
    }

    public void setCvv(int cvv) {
        this.cvv = cvv;
    }
    public int getCard_no() {
        return card_no;
    }

    public void setCard_no(int card_no) {
        this.card_no = card_no;
    }

    public Guest getGuest() {
        return guest;
    }

    public void setGuest(Guest guest) {
        this.guest = guest;
    }
    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }

}