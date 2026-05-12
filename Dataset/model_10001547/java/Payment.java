





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int paytm;
    private int pay_hotel;
    private int debit_card;
    private int credit_card;



    public Payment(
        int paytm,        int pay_hotel,        int debit_card,        int credit_card    ) {
        this.paytm = paytm;
        this.pay_hotel = pay_hotel;
        this.debit_card = debit_card;
        this.credit_card = credit_card;
    }


    public int getPaytm() {
        return paytm;
    }

    public void setPaytm(int paytm) {
        this.paytm = paytm;
    }
    public int getPay_hotel() {
        return pay_hotel;
    }

    public void setPay_hotel(int pay_hotel) {
        this.pay_hotel = pay_hotel;
    }
    public int getDebit_card() {
        return debit_card;
    }

    public void setDebit_card(int debit_card) {
        this.debit_card = debit_card;
    }
    public int getCredit_card() {
        return credit_card;
    }

    public void setCredit_card(int credit_card) {
        this.credit_card = credit_card;
    }


}