





import java.util.List;
import java.util.ArrayList;

public class dutycalls_model_Dealer_SINGLEPLAYER  {

    private int openBet;
    private None userList;
    private None main_userList;
    private int tableValue;
    private int bet;
    private None deck;
    private boolean allIn;



    public dutycalls_model_Dealer_SINGLEPLAYER(
        int openBet,        None userList,        None main_userList,        int tableValue,        int bet,        None deck,        boolean allIn    ) {
        this.openBet = openBet;
        this.userList = userList;
        this.main_userList = main_userList;
        this.tableValue = tableValue;
        this.bet = bet;
        this.deck = deck;
        this.allIn = allIn;
    }


    public int getOpenbet() {
        return openBet;
    }

    public void setOpenbet(int openBet) {
        this.openBet = openBet;
    }
    public None getUserlist() {
        return userList;
    }

    public void setUserlist(None userList) {
        this.userList = userList;
    }
    public None getMain_userlist() {
        return main_userList;
    }

    public void setMain_userlist(None main_userList) {
        this.main_userList = main_userList;
    }
    public int getTablevalue() {
        return tableValue;
    }

    public void setTablevalue(int tableValue) {
        this.tableValue = tableValue;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public boolean getAllin() {
        return allIn;
    }

    public void setAllin(boolean allIn) {
        this.allIn = allIn;
    }


}