





import java.util.List;
import java.util.ArrayList;

public class dutycalls_model_Dealer_SINGLEPLAYER  {

    private None userList;
    private None main_userList;
    private int bet;
    private int tableValue;
    private int openBet;
    private boolean allIn;
    private None deck;



    public dutycalls_model_Dealer_SINGLEPLAYER(
        None userList,        None main_userList,        int bet,        int tableValue,        int openBet,        boolean allIn,        None deck    ) {
        this.userList = userList;
        this.main_userList = main_userList;
        this.bet = bet;
        this.tableValue = tableValue;
        this.openBet = openBet;
        this.allIn = allIn;
        this.deck = deck;
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
    public int getTablevalue() {
        return tableValue;
    }

    public void setTablevalue(int tableValue) {
        this.tableValue = tableValue;
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
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }


}