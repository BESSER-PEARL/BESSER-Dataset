





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Points___Special_Offers  {

    private int Discount;





    private Online_Shopping_Customer_Account online_shopping_customer_account;


    public Online_Shopping_Points___Special_Offers(
        int Discount    ) {
        this.Discount = Discount;
    }


    public int getDiscount() {
        return Discount;
    }

    public void setDiscount(int Discount) {
        this.Discount = Discount;
    }

    public Online_Shopping_Customer_Account getOnline_shopping_customer_account() {
        return online_shopping_customer_account;
    }

    public void setOnline_shopping_customer_account(Online_Shopping_Customer_Account online_shopping_customer_account) {
        this.online_shopping_customer_account = online_shopping_customer_account;
    }

}