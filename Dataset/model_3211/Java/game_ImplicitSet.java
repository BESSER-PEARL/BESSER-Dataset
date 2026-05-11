





import java.util.List;
import java.util.ArrayList;

public class game_ImplicitSet extends Collection {






    private game_Expression game_expression;




    private game_Variable game_variable;


    public game_ImplicitSet(
    ) {
        super(
        );
    }



    public game_Expression getGame_expression() {
        return game_expression;
    }

    public void setGame_expression(game_Expression game_expression) {
        this.game_expression = game_expression;
    }
    public game_Variable getGame_variable() {
        return game_variable;
    }

    public void setGame_variable(game_Variable game_variable) {
        this.game_variable = game_variable;
    }

}