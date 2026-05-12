





import java.util.List;
import java.util.ArrayList;

public class table_Table  {

    private int amountOfCards;
    private None upcomingCards;
    private String turnedCards;





    private table_Deck table_deck;




    private table_Card table_card;




    private player_Players player_players;




    private managers_GameManager managers_gamemanager;


    public table_Table(
        int amountOfCards,        None upcomingCards,        String turnedCards    ) {
        this.amountOfCards = amountOfCards;
        this.upcomingCards = upcomingCards;
        this.turnedCards = turnedCards;
    }


    public int getAmountofcards() {
        return amountOfCards;
    }

    public void setAmountofcards(int amountOfCards) {
        this.amountOfCards = amountOfCards;
    }
    public None getUpcomingcards() {
        return upcomingCards;
    }

    public void setUpcomingcards(None upcomingCards) {
        this.upcomingCards = upcomingCards;
    }
    public String getTurnedcards() {
        return turnedCards;
    }

    public void setTurnedcards(String turnedCards) {
        this.turnedCards = turnedCards;
    }

    public table_Deck getTable_deck() {
        return table_deck;
    }

    public void setTable_deck(table_Deck table_deck) {
        this.table_deck = table_deck;
    }
    public table_Card getTable_card() {
        return table_card;
    }

    public void setTable_card(table_Card table_card) {
        this.table_card = table_card;
    }
    public player_Players getPlayer_players() {
        return player_players;
    }

    public void setPlayer_players(player_Players player_players) {
        this.player_players = player_players;
    }
    public managers_GameManager getManagers_gamemanager() {
        return managers_gamemanager;
    }

    public void setManagers_gamemanager(managers_GameManager managers_gamemanager) {
        this.managers_gamemanager = managers_gamemanager;
    }

}