





import java.util.List;
import java.util.ArrayList;

public class account_UserAccount  {

    private String createdAt;
    private String gamesWon;
    private String alias;
    private String password;
    private String email;
    private String id;
    private String gamesPlayed;



    public account_UserAccount(
        String createdAt,        String gamesWon,        String alias,        String password,        String email,        String id,        String gamesPlayed    ) {
        this.createdAt = createdAt;
        this.gamesWon = gamesWon;
        this.alias = alias;
        this.password = password;
        this.email = email;
        this.id = id;
        this.gamesPlayed = gamesPlayed;
    }


    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String getGameswon() {
        return gamesWon;
    }

    public void setGameswon(String gamesWon) {
        this.gamesWon = gamesWon;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getGamesplayed() {
        return gamesPlayed;
    }

    public void setGamesplayed(String gamesPlayed) {
        this.gamesPlayed = gamesPlayed;
    }


}