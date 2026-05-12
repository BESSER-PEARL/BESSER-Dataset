





import java.util.List;
import java.util.ArrayList;

public class Session  {

    private String cardDeck;
    private String players;
    private int currentPlayerPointer;
    private int humanPointer;
    private boolean humanTurn;
    private String discardPile;
    private String gameStatus;
    private int gameStatusCode;
    private int id;





    private Player player;




    private Card card;


    public Session(
        String cardDeck,        String players,        int currentPlayerPointer,        int humanPointer,        boolean humanTurn,        String discardPile,        String gameStatus,        int gameStatusCode,        int id    ) {
        this.cardDeck = cardDeck;
        this.players = players;
        this.currentPlayerPointer = currentPlayerPointer;
        this.humanPointer = humanPointer;
        this.humanTurn = humanTurn;
        this.discardPile = discardPile;
        this.gameStatus = gameStatus;
        this.gameStatusCode = gameStatusCode;
        this.id = id;
    }


    public String getCarddeck() {
        return cardDeck;
    }

    public void setCarddeck(String cardDeck) {
        this.cardDeck = cardDeck;
    }
    public String getPlayers() {
        return players;
    }

    public void setPlayers(String players) {
        this.players = players;
    }
    public int getCurrentplayerpointer() {
        return currentPlayerPointer;
    }

    public void setCurrentplayerpointer(int currentPlayerPointer) {
        this.currentPlayerPointer = currentPlayerPointer;
    }
    public int getHumanpointer() {
        return humanPointer;
    }

    public void setHumanpointer(int humanPointer) {
        this.humanPointer = humanPointer;
    }
    public boolean getHumanturn() {
        return humanTurn;
    }

    public void setHumanturn(boolean humanTurn) {
        this.humanTurn = humanTurn;
    }
    public String getDiscardpile() {
        return discardPile;
    }

    public void setDiscardpile(String discardPile) {
        this.discardPile = discardPile;
    }
    public String getGamestatus() {
        return gameStatus;
    }

    public void setGamestatus(String gameStatus) {
        this.gameStatus = gameStatus;
    }
    public int getGamestatuscode() {
        return gameStatusCode;
    }

    public void setGamestatuscode(int gameStatusCode) {
        this.gameStatusCode = gameStatusCode;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }
    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }

}