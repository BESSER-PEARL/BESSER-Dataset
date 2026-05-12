





import java.util.List;
import java.util.ArrayList;

public class account_UserAccountPublicInfo  {

    private String gamesPlayed;
    private String alias;
    private String gamesWon;
    private String id;





    private account_UserAccountController account_useraccountcontroller;


    public account_UserAccountPublicInfo(
        String gamesPlayed,        String alias,        String gamesWon,        String id    ) {
        this.gamesPlayed = gamesPlayed;
        this.alias = alias;
        this.gamesWon = gamesWon;
        this.id = id;
    }


    public String getGamesplayed() {
        return gamesPlayed;
    }

    public void setGamesplayed(String gamesPlayed) {
        this.gamesPlayed = gamesPlayed;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getGameswon() {
        return gamesWon;
    }

    public void setGameswon(String gamesWon) {
        this.gamesWon = gamesWon;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public account_UserAccountController getAccount_useraccountcontroller() {
        return account_useraccountcontroller;
    }

    public void setAccount_useraccountcontroller(account_UserAccountController account_useraccountcontroller) {
        this.account_useraccountcontroller = account_useraccountcontroller;
    }

}