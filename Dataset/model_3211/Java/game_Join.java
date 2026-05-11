





import java.util.List;
import java.util.ArrayList;

public class game_Join extends Collection {






    private List<game_Expression> game_expressions;


    public game_Join(
    ) {
        super(
        );
        this.game_expressions = new ArrayList<>();
    }

    public game_Join(
        ArrayList<game_Expression> game_expressions    ) {
        this.game_expressions = game_expressions;
    }


    public List<game_Expression> getGame_expressions() {
        return game_expressions;
    }

    public void addGame_expression(Game_expression game_expression) {
        this.game_expressions.add(game_expression);
    }

}