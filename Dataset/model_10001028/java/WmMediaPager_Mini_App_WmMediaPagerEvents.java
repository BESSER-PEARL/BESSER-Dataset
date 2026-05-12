




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class WmMediaPager_Mini_App_WmMediaPagerEvents  {

    private LocalDate transactionTime;
    private int id;
    private float amount;
    private None type;



    public WmMediaPager_Mini_App_WmMediaPagerEvents(
        LocalDate transactionTime,        int id,        float amount,        None type    ) {
        this.transactionTime = transactionTime;
        this.id = id;
        this.amount = amount;
        this.type = type;
    }


    public LocalDate getTransactiontime() {
        return transactionTime;
    }

    public void setTransactiontime(LocalDate transactionTime) {
        this.transactionTime = transactionTime;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }


}