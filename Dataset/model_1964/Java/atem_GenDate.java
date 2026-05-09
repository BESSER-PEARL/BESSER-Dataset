





import java.util.List;
import java.util.ArrayList;

public class atem_GenDate extends LdpType {

    private boolean dsl_Display_Date;



    public atem_GenDate(
        boolean dsl_Display_Date    ) {
        super(
        );
        this.dsl_Display_Date = dsl_Display_Date;
    }


    public boolean getDsl_display_date() {
        return dsl_Display_Date;
    }

    public void setDsl_display_date(boolean dsl_Display_Date) {
        this.dsl_Display_Date = dsl_Display_Date;
    }


}