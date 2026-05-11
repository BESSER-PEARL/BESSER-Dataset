





import java.util.List;
import java.util.ArrayList;

public class game_Type  {

    private boolean valueType;
    private String name;
    private String namespace;





    private List<game_Type> game_types;




    private game_Game game_game;


    public game_Type(
        boolean valueType,        String name,        String namespace    ) {
        this.valueType = valueType;
        this.name = name;
        this.namespace = namespace;
        this.game_types = new ArrayList<>();
    }

    public game_Type(
        boolean valueType,        String name,        String namespace        ArrayList<game_Type> game_types    ) {
        this.valueType = valueType;
        this.name = name;
        this.namespace = namespace;
        this.game_types = game_types;
    }

    public boolean getValuetype() {
        return valueType;
    }

    public void setValuetype(boolean valueType) {
        this.valueType = valueType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public List<game_Type> getGame_types() {
        return game_types;
    }

    public void addGame_type(Game_type game_type) {
        this.game_types.add(game_type);
    }
    public game_Game getGame_game() {
        return game_game;
    }

    public void setGame_game(game_Game game_game) {
        this.game_game = game_game;
    }

}