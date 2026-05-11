





import java.util.List;
import java.util.ArrayList;

public class myDsl_LEFT extends CMD {

    private int amount;



    public myDsl_LEFT(
        int amount    ) {
        super(
        );
        this.amount = amount;
    }


    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }


}