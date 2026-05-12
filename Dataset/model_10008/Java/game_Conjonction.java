





import java.util.List;
import java.util.ArrayList;

public class game_Conjonction  {






    private game_Condition game_condition;




    private List<game_Litteral> game_litterals;


    public game_Conjonction(
    ) {
        this.game_litterals = new ArrayList<>();
    }

    public game_Conjonction(
        ArrayList<game_Litteral> game_litterals    ) {
        this.game_litterals = game_litterals;
    }


    public game_Condition getGame_condition() {
        return game_condition;
    }

    public void setGame_condition(game_Condition game_condition) {
        this.game_condition = game_condition;
    }
    public List<game_Litteral> getGame_litterals() {
        return game_litterals;
    }

    public void addGame_litteral(Game_litteral game_litteral) {
        this.game_litterals.add(game_litteral);
    }

}