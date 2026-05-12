





import java.util.List;
import java.util.ArrayList;

public class dutycalls_contoller_Dealer_Control  {

    private int cardCount;
    private int userid;



    public dutycalls_contoller_Dealer_Control(
        int cardCount,        int userid    ) {
        this.cardCount = cardCount;
        this.userid = userid;
    }


    public int getCardcount() {
        return cardCount;
    }

    public void setCardcount(int cardCount) {
        this.cardCount = cardCount;
    }
    public int getUserid() {
        return userid;
    }

    public void setUserid(int userid) {
        this.userid = userid;
    }


}