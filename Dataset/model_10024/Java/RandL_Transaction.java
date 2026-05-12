





import java.util.List;
import java.util.ArrayList;

public class RandL_Transaction  {

    private String points;
    private String amount;



    public RandL_Transaction(
        String points,        String amount    ) {
        this.points = points;
        this.amount = amount;
    }


    public String getPoints() {
        return points;
    }

    public void setPoints(String points) {
        this.points = points;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }


}