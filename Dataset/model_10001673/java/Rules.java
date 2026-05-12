





import java.util.List;
import java.util.ArrayList;

public class Rules  {

    private None card2;
    private None card3;
    private None card1;





    private List<Game> games;


    public Rules(
        None card2,        None card3,        None card1    ) {
        this.card2 = card2;
        this.card3 = card3;
        this.card1 = card1;
        this.games = new ArrayList<>();
    }

    public Rules(
        None card2,        None card3,        None card1        ArrayList<Game> games    ) {
        this.card2 = card2;
        this.card3 = card3;
        this.card1 = card1;
        this.games = games;
    }

    public None getCard2() {
        return card2;
    }

    public void setCard2(None card2) {
        this.card2 = card2;
    }
    public None getCard3() {
        return card3;
    }

    public void setCard3(None card3) {
        this.card3 = card3;
    }
    public None getCard1() {
        return card1;
    }

    public void setCard1(None card1) {
        this.card1 = card1;
    }

    public List<Game> getGames() {
        return games;
    }

    public void addGame(Game game) {
        this.games.add(game);
    }

}