





import java.util.List;
import java.util.ArrayList;

public class dutycalls_model_Dealer_SINGLEPLAYER  {

    private None deck;
    private int tableValue;
    private None userList;
    private None main_userList;
    private int bet;
    private boolean allIn;
    private int openBet;



    public dutycalls_model_Dealer_SINGLEPLAYER(
        None deck,        int tableValue,        None userList,        None main_userList,        int bet,        boolean allIn,        int openBet    ) {
        this.deck = deck;
        this.tableValue = tableValue;
        this.userList = userList;
        this.main_userList = main_userList;
        this.bet = bet;
        this.allIn = allIn;
        this.openBet = openBet;
    }


    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public int getTablevalue() {
        return tableValue;
    }

    public void setTablevalue(int tableValue) {
        this.tableValue = tableValue;
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