





import java.util.List;
import java.util.ArrayList;

public class game_System  {

    private String name;





    private List<game_Statement> game_statements;




    private List<game_Query> game_querys;




    private game_Game game_game;


    public game_System(
        String name    ) {
        this.name = name;
        this.game_statements = new ArrayList<>();
        this.game_querys = new ArrayList<>();
    }

    public game_System(
        String name        ArrayList<game_Statement> game_statements,        ArrayList<game_Query> game_querys    ) {
        this.name = name;
        this.game_statements = game_statements;
        this.game_querys = game_querys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<game_Statement> getGame_statements() {
        return game_statements;
    }

    public void addGame_statement(Game_statement game_statement) {
        this.game_statements.add(game_statement);
    }
    public List<game_Query> getGame_querys() {
        return game_querys;
    }

    public void addGame_query(Game_query game_query) {
        this.game_querys.add(game_query);
    }
    public game_Game getGame_game() {
        return game_game;
    }

    public void setGame_game(game_Game game_game) {
        this.game_game = game_game;
    }

}