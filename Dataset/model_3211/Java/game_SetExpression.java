





import java.util.List;
import java.util.ArrayList;

public class game_SetExpression extends Setable {






    private game_Primary game_primary;




    private game_Setable game_setable;


    public game_SetExpression(
    ) {
        super(
        );
    }



    public game_Primary getGame_primary() {
        return game_primary;
    }

    public void setGame_primary(game_Primary game_primary) {
        this.game_primary = game_primary;
    }
    public game_Setable getGame_setable() {
        return game_setable;
    }

    public void setGame_setable(game_Setable game_setable) {
        this.game_setable = game_setable;
    }

}