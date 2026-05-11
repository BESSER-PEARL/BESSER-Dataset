





import java.util.List;
import java.util.ArrayList;

public class game_Variable extends Atom {

    private String name;





    private game_Forall game_forall;


    public game_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public game_Forall getGame_forall() {
        return game_forall;
    }

    public void setGame_forall(game_Forall game_forall) {
        this.game_forall = game_forall;
    }

}