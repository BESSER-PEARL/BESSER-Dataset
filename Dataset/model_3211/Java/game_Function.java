





import java.util.List;
import java.util.ArrayList;

public class game_Function  {

    private String name;





    private game_Game game_game;




    private game_Type game_type;




    private List<game_Statement> game_statements;


    public game_Function(
        String name    ) {
        this.name = name;
        this.game_statements = new ArrayList<>();
    }

    public game_Function(
        String name        ArrayList<game_Statement> game_statements    ) {
        this.name = name;
        this.game_statements = game_statements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public game_Game getGame_game() {
        return game_game;
    }

    public void setGame_game(game_Game game_game) {
        this.game_game = game_game;
    }
    public game_Type getGame_type() {
        return game_type;
    }

    public void setGame_type(game_Type game_type) {
        this.game_type = game_type;
    }
    public List<game_Statement> getGame_statements() {
        return game_statements;
    }

    public void addGame_statement(Game_statement game_statement) {
        this.game_statements.add(game_statement);
    }

}