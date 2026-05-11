





import java.util.List;
import java.util.ArrayList;

public class game_Access  {

    private String name;
    private String kind;





    private game_Query game_query;


    public game_Access(
        String name,        String kind    ) {
        this.name = name;
        this.kind = kind;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public game_Query getGame_query() {
        return game_query;
    }

    public void setGame_query(game_Query game_query) {
        this.game_query = game_query;
    }

}