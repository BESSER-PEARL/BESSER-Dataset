





import java.util.List;
import java.util.ArrayList;

public class atem_DayRange extends AbstractDayCase {

    private int dsl_DayRange_from;
    private int dsl_Range_To;



    public atem_DayRange(
        int dsl_DayRange_from,        int dsl_Range_To    ) {
        super(
        );
        this.dsl_DayRange_from = dsl_DayRange_from;
        this.dsl_Range_To = dsl_Range_To;
    }


    public int getDsl_dayrange_from() {
        return dsl_DayRange_from;
    }

    public void setDsl_dayrange_from(int dsl_DayRange_from) {
        this.dsl_DayRange_from = dsl_DayRange_from;
    }
    public int getDsl_range_to() {
        return dsl_Range_To;
    }

    public void setDsl_range_to(int dsl_Range_To) {
        this.dsl_Range_To = dsl_Range_To;
    }


}