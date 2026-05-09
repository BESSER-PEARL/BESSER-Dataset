





import java.util.List;
import java.util.ArrayList;

public class atem_DayNameRange extends AbstractDayNameCase {

    private String dsl_DayNameRange_from;
    private String dsl_DayNameRange_To;



    public atem_DayNameRange(
        String dsl_DayNameRange_from,        String dsl_DayNameRange_To    ) {
        super(
        );
        this.dsl_DayNameRange_from = dsl_DayNameRange_from;
        this.dsl_DayNameRange_To = dsl_DayNameRange_To;
    }


    public String getDsl_daynamerange_from() {
        return dsl_DayNameRange_from;
    }

    public void setDsl_daynamerange_from(String dsl_DayNameRange_from) {
        this.dsl_DayNameRange_from = dsl_DayNameRange_from;
    }
    public String getDsl_daynamerange_to() {
        return dsl_DayNameRange_To;
    }

    public void setDsl_daynamerange_to(String dsl_DayNameRange_To) {
        this.dsl_DayNameRange_To = dsl_DayNameRange_To;
    }


}