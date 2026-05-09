





import java.util.List;
import java.util.ArrayList;

public class atem_DateRange extends AbstractDateCase {

    private int dsl_DateRange_To;
    private int dsl_DateRange_from;



    public atem_DateRange(
        int dsl_DateRange_To,        int dsl_DateRange_from    ) {
        super(
        );
        this.dsl_DateRange_To = dsl_DateRange_To;
        this.dsl_DateRange_from = dsl_DateRange_from;
    }


    public int getDsl_daterange_to() {
        return dsl_DateRange_To;
    }

    public void setDsl_daterange_to(int dsl_DateRange_To) {
        this.dsl_DateRange_To = dsl_DateRange_To;
    }
    public int getDsl_daterange_from() {
        return dsl_DateRange_from;
    }

    public void setDsl_daterange_from(int dsl_DateRange_from) {
        this.dsl_DateRange_from = dsl_DateRange_from;
    }


}