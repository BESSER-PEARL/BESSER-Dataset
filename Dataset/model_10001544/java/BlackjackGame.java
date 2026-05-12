





import java.util.List;
import java.util.ArrayList;

public class BlackjackGame  {






    private _Interface _interface;




    private Dealer dealer;




    private Player player;


    public BlackjackGame(
    ) {
    }



    public _Interface get_interface() {
        return _interface;
    }

    public void set_interface(_Interface _interface) {
        this._interface = _interface;
    }
    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}