





import java.util.List;
import java.util.ArrayList;

public class game_Addition extends Addable {

    private String kind;





    private game_Multipliable game_multipliable;




    private game_Addable game_addable;


    public game_Addition(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public game_Multipliable getGame_multipliable() {
        return game_multipliable;
    }

    public void setGame_multipliable(game_Multipliable game_multipliable) {
        this.game_multipliable = game_multipliable;
    }
    public game_Addable getGame_addable() {
        return game_addable;
    }

    public void setGame_addable(game_Addable game_addable) {
        this.game_addable = game_addable;
    }

}