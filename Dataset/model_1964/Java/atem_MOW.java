





import java.util.List;
import java.util.ArrayList;

public class atem_MOW extends LdpType {

    private boolean dsl_Display_Mode;



    public atem_MOW(
        boolean dsl_Display_Mode    ) {
        super(
        );
        this.dsl_Display_Mode = dsl_Display_Mode;
    }


    public boolean getDsl_display_mode() {
        return dsl_Display_Mode;
    }

    public void setDsl_display_mode(boolean dsl_Display_Mode) {
        this.dsl_Display_Mode = dsl_Display_Mode;
    }


}