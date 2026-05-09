





import java.util.List;
import java.util.ArrayList;

public class budgeting_CashTransaction extends Transaction {

    private String day;



    public budgeting_CashTransaction(
        String day    ) {
        super(
        );
        this.day = day;
    }


    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }


}