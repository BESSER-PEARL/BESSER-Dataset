





import java.util.List;
import java.util.ArrayList;

public class BlackJack_Hra  {

    private String dealer_wins;
    private String placebet;
    private String deal;
    private String player_asks_for_card;
    private String deck;
    private String dealers_hand;
    private String play;
    private String tie;
    private String players_hand;
    private String bet;
    private String player_wins;
    private String show_result;
    private String money;





    private BlackJackApp blackjackapp;


    public BlackJack_Hra(
        String dealer_wins,        String placebet,        String deal,        String player_asks_for_card,        String deck,        String dealers_hand,        String play,        String tie,        String players_hand,        String bet,        String player_wins,        String show_result,        String money    ) {
        this.dealer_wins = dealer_wins;
        this.placebet = placebet;
        this.deal = deal;
        this.player_asks_for_card = player_asks_for_card;
        this.deck = deck;
        this.dealers_hand = dealers_hand;
        this.play = play;
        this.tie = tie;
        this.players_hand = players_hand;
        this.bet = bet;
        this.player_wins = player_wins;
        this.show_result = show_result;
        this.money = money;
    }


    public String getDealer_wins() {
        return dealer_wins;
    }

    public void setDealer_wins(String dealer_wins) {
        this.dealer_wins = dealer_wins;
    }
    public String getPlacebet() {
        return placebet;
    }

    public void setPlacebet(String placebet) {
        this.placebet = placebet;
    }
    public String getDeal() {
        return deal;
    }

    public void setDeal(String deal) {
        this.deal = deal;
    }
    public String getPlayer_asks_for_card() {
        return player_asks_for_card;
    }

    public void setPlayer_asks_for_card(String player_asks_for_card) {
        this.player_asks_for_card = player_asks_for_card;
    }
    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public String getDealers_hand() {
        return dealers_hand;
    }

    public void setDealers_hand(String dealers_hand) {
        this.dealers_hand = dealers_hand;
    }
    public String getPlay() {
        return play;
    }

    public void setPlay(String play) {
        this.play = play;
    }
    public String getTie() {
        return tie;
    }

    public void setTie(String tie) {
        this.tie = tie;
    }
    public String getPlayers_hand() {
        return players_hand;
    }

    public void setPlayers_hand(String players_hand) {
        this.players_hand = players_hand;
    }
    public String getBet() {
        return bet;
    }

    public void setBet(String bet) {
        this.bet = bet;
    }
    public String getPlayer_wins() {
        return player_wins;
    }

    public void setPlayer_wins(String player_wins) {
        this.player_wins = player_wins;
    }
    public String getShow_result() {
        return show_result;
    }

    public void setShow_result(String show_result) {
        this.show_result = show_result;
    }
    public String getMoney() {
        return money;
    }

    public void setMoney(String money) {
        this.money = money;
    }

    public BlackJackApp getBlackjackapp() {
        return blackjackapp;
    }

    public void setBlackjackapp(BlackJackApp blackjackapp) {
        this.blackjackapp = blackjackapp;
    }

}