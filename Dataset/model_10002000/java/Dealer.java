





import java.util.List;
import java.util.ArrayList;

public class Dealer  {

    private String shuffle__;
    private String Dealer__;
    private String Dealer__1;
    private String distribute_Player___;



    public Dealer(
        String shuffle__,        String Dealer__,        String Dealer__1,        String distribute_Player___    ) {
        this.shuffle__ = shuffle__;
        this.Dealer__ = Dealer__;
        this.Dealer__1 = Dealer__1;
        this.distribute_Player___ = distribute_Player___;
    }


    public String getShuffle__() {
        return shuffle__;
    }

    public void setShuffle__(String shuffle__) {
        this.shuffle__ = shuffle__;
    }
    public String getDealer__() {
        return Dealer__;
    }

    public void setDealer__(String Dealer__) {
        this.Dealer__ = Dealer__;
    }
    public String getDealer__1() {
        return Dealer__1;
    }

    public void setDealer__1(String Dealer__1) {
        this.Dealer__1 = Dealer__1;
    }
    public String getDistribute_player___() {
        return distribute_Player___;
    }

    public void setDistribute_player___(String distribute_Player___) {
        this.distribute_Player___ = distribute_Player___;
    }


}