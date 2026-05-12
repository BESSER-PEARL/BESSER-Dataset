





import java.util.List;
import java.util.ArrayList;

public class Match  {

    private String date;
    private None winner;
    private String players;
    private String name;



    public Match(
        String date,        None winner,        String players,        String name    ) {
        this.date = date;
        this.winner = winner;
        this.players = players;
        this.name = name;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public None getWinner() {
        return winner;
    }

    public void setWinner(None winner) {
        this.winner = winner;
    }
    public String getPlayers() {
        return players;
    }

    public void setPlayers(String players) {
        this.players = players;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}