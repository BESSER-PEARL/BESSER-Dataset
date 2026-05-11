




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bowling_Tournament  {

    private boolean receivesTrophy;
    private float priceMoney;
    private String type;
    private LocalDate matchDays;



    public bowling_Tournament(
        boolean receivesTrophy,        float priceMoney,        String type,        LocalDate matchDays    ) {
        this.receivesTrophy = receivesTrophy;
        this.priceMoney = priceMoney;
        this.type = type;
        this.matchDays = matchDays;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public LocalDate getMatchdays() {
        return matchDays;
    }

    public void setMatchdays(LocalDate matchDays) {
        this.matchDays = matchDays;
    }


}