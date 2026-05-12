





import java.util.List;
import java.util.ArrayList;

public class dutycalls_model_Dealer_SINGLEPLAYER  {

    private None main_userList;
    private None deck;
    private None userList;
    private int tableValue;
    private int bet;
    private boolean allIn;
    private int openBet;



    public dutycalls_model_Dealer_SINGLEPLAYER(
        None main_userList,        None deck,        None userList,        int tableValue,        int bet,        boolean allIn,        int openBet    ) {
        this.main_userList = main_userList;
        this.deck = deck;
        this.userList = userList;
        this.tableValue = tableValue;
        this.bet = bet;
        this.allIn = allIn;
        this.openBet = openBet;
    }


    public None getMain_userlist() {
        return main_userList;
    }

    public void setMain_userlist(None main_userList) {
        this.main_userList = main_userList;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public None getUserlist() {
        return userList;
    }

    public void setUserlist(None userList) {
        this.userList = userList;
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
    public boolean getAllin() {
        return allIn;
    }

    public void setAllin(boolean allIn) {
        this.allIn = allIn;
    }
    public int getOpenbet() {
        return openBet;
    }

    public void setOpenbet(int openBet) {
        this.openBet = openBet;
    }


}