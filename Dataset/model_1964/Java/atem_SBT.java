





import java.util.List;
import java.util.ArrayList;

public class atem_SBT extends LdpType {

    private boolean dsl_Display_SundaysBeforeTriodion;



    public atem_SBT(
        boolean dsl_Display_SundaysBeforeTriodion    ) {
        super(
        );
        this.dsl_Display_SundaysBeforeTriodion = dsl_Display_SundaysBeforeTriodion;
    }


    public boolean getDsl_display_sundaysbeforetriodion() {
        return dsl_Display_SundaysBeforeTriodion;
    }

    public void setDsl_display_sundaysbeforetriodion(boolean dsl_Display_SundaysBeforeTriodion) {
        this.dsl_Display_SundaysBeforeTriodion = dsl_Display_SundaysBeforeTriodion;
    }


}