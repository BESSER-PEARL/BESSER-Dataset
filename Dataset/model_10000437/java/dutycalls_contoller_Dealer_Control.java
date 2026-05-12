





import java.util.List;
import java.util.ArrayList;

public class dutycalls_contoller_Dealer_Control  {

    private int userid;
    private int cardCount;



    public dutycalls_contoller_Dealer_Control(
        int userid,        int cardCount    ) {
        this.userid = userid;
        this.cardCount = cardCount;
    }


    public int getUserid() {
        return userid;
    }

    public void setUserid(int userid) {
        this.userid = userid;
    }
    public int getCardcount() {
        return cardCount;
    }

    public void setCardcount(int cardCount) {
        this.cardCount = cardCount;
    }


}