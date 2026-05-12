





import java.util.List;
import java.util.ArrayList;

public class Bank  {

    private int Account_no;
    private String Online_payment_ID_and_password;
    private String Account_type;



    public Bank(
        int Account_no,        String Online_payment_ID_and_password,        String Account_type    ) {
        this.Account_no = Account_no;
        this.Online_payment_ID_and_password = Online_payment_ID_and_password;
        this.Account_type = Account_type;
    }


    public int getAccount_no() {
        return Account_no;
    }

    public void setAccount_no(int Account_no) {
        this.Account_no = Account_no;
    }
    public String getOnline_payment_id_and_password() {
        return Online_payment_ID_and_password;
    }

    public void setOnline_payment_id_and_password(String Online_payment_ID_and_password) {
        this.Online_payment_ID_and_password = Online_payment_ID_and_password;
    }
    public String getAccount_type() {
        return Account_type;
    }

    public void setAccount_type(String Account_type) {
        this.Account_type = Account_type;
    }


}