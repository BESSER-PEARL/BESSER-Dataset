





import java.util.List;
import java.util.ArrayList;

public class Blackjack_Stay_UseCase  {






    private Player_Actor player_actor;




    private Dealer_Actor dealer_actor;


    public Blackjack_Stay_UseCase(
    ) {
    }



    public Player_Actor getPlayer_actor() {
        return player_actor;
    }

    public void setPlayer_actor(Player_Actor player_actor) {
        this.player_actor = player_actor;
    }
    public Dealer_Actor getDealer_actor() {
        return dealer_actor;
    }

    public void setDealer_actor(Dealer_Actor dealer_actor) {
        this.dealer_actor = dealer_actor;
    }

}