





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String name;





    private List<Card> cards;




    private Avatar avatar;




    private List<Game> games;


    public Player(
        String name    ) {
        this.name = name;
        this.cards = new ArrayList<>();
        this.games = new ArrayList<>();
    }

    public Player(
        String name        ArrayList<Card> cards,        ArrayList<Game> games    ) {
        this.name = name;
        this.cards = cards;
        this.games = games;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }
    public Avatar getAvatar() {
        return avatar;
    }

    public void setAvatar(Avatar avatar) {
        this.avatar = avatar;
    }
    public List<Game> getGames() {
        return games;
    }

    public void addGame(Game game) {
        this.games.add(game);
    }

}