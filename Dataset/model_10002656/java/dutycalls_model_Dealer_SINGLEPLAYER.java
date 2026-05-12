





import java.util.List;
import java.util.ArrayList;

public class dutycalls_model_Dealer_SINGLEPLAYER  {

    private None deck;
    private int openBet;
    private boolean allIn;
    private int tableValue;
    private None main_userList;
    private None userList;
    private int bet;



    public dutycalls_model_Dealer_SINGLEPLAYER(
        None deck,        int openBet,        boolean allIn,        int tableValue,        None main_userList,        None userList,        int bet    ) {
        this.deck = deck;
        this.openBet = openBet;
        this.allIn = allIn;
        this.tableValue = tableValue;
        this.main_userList = main_userList;
        this.userList = userList;
        this.bet = bet;
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
    public boolean getAllin() {
        return allIn;
    }

    public void setAllin(boolean allIn) {
        this.allIn = allIn;
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
    public None getUserlist() {
        return userList;
    }

    public void setUserlist(None userList) {
        this.userList = userList;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }


}