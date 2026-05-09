





import java.util.List;
import java.util.ArrayList;

public class budgeting_CardTransaction extends Transaction {

    private String from_;
    private int day;



    public budgeting_CardTransaction(
        String from_,        int day    ) {
        super(
        );
        this.from_ = from_;
        this.day = day;
    }


    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }


}