





import java.util.List;
import java.util.ArrayList;

public class game_Forall extends Statement {






    private List<game_Statement> game_statements;


    public game_Forall(
    ) {
        super(
        );
        this.game_statements = new ArrayList<>();
    }

    public game_Forall(
        ArrayList<game_Statement> game_statements    ) {
        this.game_statements = game_statements;
    }


    public List<game_Statement> getGame_statements() {
        return game_statements;
    }

    public void addGame_statement(Game_statement game_statement) {
        this.game_statements.add(game_statement);
    }

}