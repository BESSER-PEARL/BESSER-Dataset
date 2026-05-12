





import java.util.List;
import java.util.ArrayList;

public class PokerTable  {






    private List<Player> players;




    private List<PlayCard> playcards;




    private Player player;


    public PokerTable(
    ) {
        this.players = new ArrayList<>();
        this.playcards = new ArrayList<>();
    }

    public PokerTable(
        ArrayList<Player> players,        ArrayList<PlayCard> playcards    ) {
        this.players = players;
        this.playcards = playcards;
    }


    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
    }
    public List<PlayCard> getPlaycards() {
        return playcards;
    }

    public void addPlaycard(Playcard playcard) {
        this.playcards.add(playcard);
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}