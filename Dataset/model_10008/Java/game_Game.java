





import java.util.List;
import java.util.ArrayList;

public class game_Game  {

    private String name;





    private game_Lieu game_lieu;




    private List<game_Lieu> game_lieus;


    public game_Game(
        String name    ) {
        this.name = name;
        this.game_lieus = new ArrayList<>();
    }

    public game_Game(
        String name        ArrayList<game_Lieu> game_lieus    ) {
        this.name = name;
        this.game_lieus = game_lieus;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public game_Lieu getGame_lieu() {
        return game_lieu;
    }

    public void setGame_lieu(game_Lieu game_lieu) {
        this.game_lieu = game_lieu;
    }
    public List<game_Lieu> getGame_lieus() {
        return game_lieus;
    }

    public void addGame_lieu(Game_lieu game_lieu) {
        this.game_lieus.add(game_lieu);
    }

}