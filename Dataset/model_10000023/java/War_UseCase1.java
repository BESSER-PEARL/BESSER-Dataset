





import java.util.List;
import java.util.ArrayList;

public class War_UseCase1  {






    private War_UseCase war_usecase;




    private Winner_UseCase winner_usecase;


    public War_UseCase1(
    ) {
    }



    public War_UseCase getWar_usecase() {
        return war_usecase;
    }

    public void setWar_usecase(War_UseCase war_usecase) {
        this.war_usecase = war_usecase;
    }
    public Winner_UseCase getWinner_usecase() {
        return winner_usecase;
    }

    public void setWinner_usecase(Winner_UseCase winner_usecase) {
        this.winner_usecase = winner_usecase;
    }

}