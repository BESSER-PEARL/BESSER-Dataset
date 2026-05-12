





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Payment  {

    private String Online_Pay;
    private String Catch_Pay;





    private online_shopping_Shopping_Card online_shopping_shopping_card;


    public online_shopping_Payment(
        String Online_Pay,        String Catch_Pay    ) {
        this.Online_Pay = Online_Pay;
        this.Catch_Pay = Catch_Pay;
    }


    public String getOnline_pay() {
        return Online_Pay;
    }

    public void setOnline_pay(String Online_Pay) {
        this.Online_Pay = Online_Pay;
    }
    public String getCatch_pay() {
        return Catch_Pay;
    }

    public void setCatch_pay(String Catch_Pay) {
        this.Catch_Pay = Catch_Pay;
    }

    public online_shopping_Shopping_Card getOnline_shopping_shopping_card() {
        return online_shopping_shopping_card;
    }

    public void setOnline_shopping_shopping_card(online_shopping_Shopping_Card online_shopping_shopping_card) {
        this.online_shopping_shopping_card = online_shopping_shopping_card;
    }

}