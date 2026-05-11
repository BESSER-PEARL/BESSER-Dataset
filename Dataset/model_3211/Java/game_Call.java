





import java.util.List;
import java.util.ArrayList;

public class game_Call extends Primary {

    private String name;





    private List<game_Expression> game_expressions;




    private game_Subprocess game_subprocess;


    public game_Call(
        String name    ) {
        super(
        );
        this.name = name;
        this.game_expressions = new ArrayList<>();
    }

    public game_Call(
        String name        ArrayList<game_Expression> game_expressions    ) {
        this.name = name;
        this.game_expressions = game_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<game_Expression> getGame_expressions() {
        return game_expressions;
    }

    public void addGame_expression(Game_expression game_expression) {
        this.game_expressions.add(game_expression);
    }
    public game_Subprocess getGame_subprocess() {
        return game_subprocess;
    }

    public void setGame_subprocess(game_Subprocess game_subprocess) {
        this.game_subprocess = game_subprocess;
    }

}