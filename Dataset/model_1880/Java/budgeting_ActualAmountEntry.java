





import java.util.List;
import java.util.ArrayList;

public class budgeting_ActualAmountEntry extends ActualEntry {

    private String amount;



    public budgeting_ActualAmountEntry(
        String amount    ) {
        super(
        );
        this.amount = amount;
    }


    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }


}