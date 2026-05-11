





import java.util.List;
import java.util.ArrayList;

public class game_Comparison extends Comparable {

    private String kind;





    private game_Comparable game_comparable;




    private game_Addable game_addable;


    public game_Comparison(
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

    public game_Comparable getGame_comparable() {
        return game_comparable;
    }

    public void setGame_comparable(game_Comparable game_comparable) {
        this.game_comparable = game_comparable;
    }
    public game_Addable getGame_addable() {
        return game_addable;
    }

    public void setGame_addable(game_Addable game_addable) {
        this.game_addable = game_addable;
    }

}