





import java.util.List;
import java.util.ArrayList;

public class game_Equality extends Equatable {

    private String kind;





    private game_Comparable game_comparable;




    private game_Equatable game_equatable;


    public game_Equality(
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
    public game_Equatable getGame_equatable() {
        return game_equatable;
    }

    public void setGame_equatable(game_Equatable game_equatable) {
        this.game_equatable = game_equatable;
    }

}