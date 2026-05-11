





import java.util.List;
import java.util.ArrayList;

public class game_Multiplication extends Multipliable {

    private String kind;





    private game_Multipliable game_multipliable;




    private game_Setable game_setable;


    public game_Multiplication(
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
    public game_Setable getGame_setable() {
        return game_setable;
    }

    public void setGame_setable(game_Setable game_setable) {
        this.game_setable = game_setable;
    }

}