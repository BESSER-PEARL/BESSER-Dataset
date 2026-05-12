





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private String status;
    private String name;
    private String id;
    private None deck;
    private String players;



    public Game(
        String status,        String name,        String id,        None deck,        String players    ) {
        this.status = status;
        this.name = name;
        this.id = id;
        this.deck = deck;
        this.players = players;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public String getPlayers() {
        return players;
    }

    public void setPlayers(String players) {
        this.players = players;
    }


}