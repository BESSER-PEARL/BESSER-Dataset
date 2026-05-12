





import java.util.List;
import java.util.ArrayList;

public class Play_UseCase  {






    private Player1_Actor player1_actor;




    private Player2_Actor player2_actor;


    public Play_UseCase(
    ) {
    }



    public Player1_Actor getPlayer1_actor() {
        return player1_actor;
    }

    public void setPlayer1_actor(Player1_Actor player1_actor) {
        this.player1_actor = player1_actor;
    }
    public Player2_Actor getPlayer2_actor() {
        return player2_actor;
    }

    public void setPlayer2_actor(Player2_Actor player2_actor) {
        this.player2_actor = player2_actor;
    }

}