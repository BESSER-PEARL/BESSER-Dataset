





import java.util.List;
import java.util.ArrayList;

public class dutycalls_model_Dealer_SINGLEPLAYER  {

    private int tableValue;
    private None main_userList;
    private int bet;
    private None userList;
    private boolean allIn;
    private None deck;
    private int openBet;



    public dutycalls_model_Dealer_SINGLEPLAYER(
        int tableValue,        None main_userList,        int bet,        None userList,        boolean allIn,        None deck,        int openBet    ) {
        this.tableValue = tableValue;
        this.main_userList = main_userList;
        this.bet = bet;
        this.userList = userList;
        this.allIn = allIn;
        this.deck = deck;
        this.openBet = openBet;
    }


    public int getTablevalue() {
        return tableValue;
    }

    public void setTablevalue(int tableValue) {
        this.tableValue = tableValue;
    }
    public None getMain_userlist() {
        return main_userList;
    }

    public void setMain_userlist(None main_userList) {
        this.main_userList = main_userList;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }
    public None getUserlist() {
        return userList;
    }

    public void setUserlist(None userList) {
        this.userList = userList;
    }
    public boolean getAllin() {
        return allIn;
    }

    public void setAllin(boolean allIn) {
        this.allIn = allIn;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public int getOpenbet() {
        return openBet;
    }

    public void setOpenbet(int openBet) {
        this.openBet = openBet;
    }


}