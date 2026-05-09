





import java.util.List;
import java.util.ArrayList;

public class atem_GenYear extends LdpType {

    private boolean dsl_Display_Year;



    public atem_GenYear(
        boolean dsl_Display_Year    ) {
        super(
        );
        this.dsl_Display_Year = dsl_Display_Year;
    }


    public boolean getDsl_display_year() {
        return dsl_Display_Year;
    }

    public void setDsl_display_year(boolean dsl_Display_Year) {
        this.dsl_Display_Year = dsl_Display_Year;
    }


}