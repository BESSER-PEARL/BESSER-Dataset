





import java.util.List;
import java.util.ArrayList;

public class Debit_Card  {

    private String Owned_By;
    private String Card_No;





    private Debit_Card debit_card;




    private Bank bank;




    private Customer customer;


    public Debit_Card(
        String Owned_By,        String Card_No    ) {
        this.Owned_By = Owned_By;
        this.Card_No = Card_No;
    }


    public String getOwned_by() {
        return Owned_By;
    }

    public void setOwned_by(String Owned_By) {
        this.Owned_By = Owned_By;
    }
    public String getCard_no() {
        return Card_No;
    }

    public void setCard_no(String Card_No) {
        this.Card_No = Card_No;
    }

    public Debit_Card getDebit_card() {
        return debit_card;
    }

    public void setDebit_card(Debit_Card debit_card) {
        this.debit_card = debit_card;
    }
    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}