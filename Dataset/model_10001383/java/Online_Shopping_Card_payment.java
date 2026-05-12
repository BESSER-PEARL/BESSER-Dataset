





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Card_payment  {

    private int CVS_number;
    private int Valid_date;
    private String payment_type;
    private String Cardholder_name;
    private int Card_number;



    public Online_Shopping_Card_payment(
        int CVS_number,        int Valid_date,        String payment_type,        String Cardholder_name,        int Card_number    ) {
        this.CVS_number = CVS_number;
        this.Valid_date = Valid_date;
        this.payment_type = payment_type;
        this.Cardholder_name = Cardholder_name;
        this.Card_number = Card_number;
    }


    public int getCvs_number() {
        return CVS_number;
    }

    public void setCvs_number(int CVS_number) {
        this.CVS_number = CVS_number;
    }
    public int getValid_date() {
        return Valid_date;
    }

    public void setValid_date(int Valid_date) {
        this.Valid_date = Valid_date;
    }
    public String getPayment_type() {
        return payment_type;
    }

    public void setPayment_type(String payment_type) {
        this.payment_type = payment_type;
    }
    public String getCardholder_name() {
        return Cardholder_name;
    }

    public void setCardholder_name(String Cardholder_name) {
        this.Cardholder_name = Cardholder_name;
    }
    public int getCard_number() {
        return Card_number;
    }

    public void setCard_number(int Card_number) {
        this.Card_number = Card_number;
    }


}