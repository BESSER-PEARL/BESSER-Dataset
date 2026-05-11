




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Tournament  {

    private LocalDate matchDays;
    private String type;
    private boolean receivesTrophy;
    private float priceMoney;





    private List<bowling_Player> bowling_players;


    public bowling_Tournament(
        LocalDate matchDays,        String type,        boolean receivesTrophy,        float priceMoney    ) {
        this.matchDays = matchDays;
        this.type = type;
        this.receivesTrophy = receivesTrophy;
        this.priceMoney = priceMoney;
        this.bowling_players = new ArrayList<>();
    }

    public bowling_Tournament(
        LocalDate matchDays,        String type,        boolean receivesTrophy,        float priceMoney        ArrayList<bowling_Player> bowling_players    ) {
        this.matchDays = matchDays;
        this.type = type;
        this.receivesTrophy = receivesTrophy;
        this.priceMoney = priceMoney;
        this.bowling_players = bowling_players;
    }

    public LocalDate getMatchdays() {
        return matchDays;
    }

    public void setMatchdays(LocalDate matchDays) {
        this.matchDays = matchDays;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getReceivestrophy() {
        return receivesTrophy;
    }

    public void setReceivestrophy(boolean receivesTrophy) {
        this.receivesTrophy = receivesTrophy;
    }
    public float getPricemoney() {
        return priceMoney;
    }

    public void setPricemoney(float priceMoney) {
        this.priceMoney = priceMoney;
    }

    public List<bowling_Player> getBowling_players() {
        return bowling_players;
    }

    public void addBowling_player(Bowling_player bowling_player) {
        this.bowling_players.add(bowling_player);
    }

}