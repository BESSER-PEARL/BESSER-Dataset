





import java.util.List;
import java.util.ArrayList;

public class atem_Lookup extends ElementType {

    private boolean dsl_Lookup_Media_Off;
    private String dsl_Lookup_OverrideDay;
    private boolean dsl_Lookup_Override_Mode_Set;
    private boolean dsl_Lookup_Override__Day_Set;
    private String dsl_Lookup_OverrideMode;



    public atem_Lookup(
        boolean dsl_Lookup_Media_Off,        String dsl_Lookup_OverrideDay,        boolean dsl_Lookup_Override_Mode_Set,        boolean dsl_Lookup_Override__Day_Set,        String dsl_Lookup_OverrideMode    ) {
        super(
        );
        this.dsl_Lookup_Media_Off = dsl_Lookup_Media_Off;
        this.dsl_Lookup_OverrideDay = dsl_Lookup_OverrideDay;
        this.dsl_Lookup_Override_Mode_Set = dsl_Lookup_Override_Mode_Set;
        this.dsl_Lookup_Override__Day_Set = dsl_Lookup_Override__Day_Set;
        this.dsl_Lookup_OverrideMode = dsl_Lookup_OverrideMode;
    }


    public boolean getDsl_lookup_media_off() {
        return dsl_Lookup_Media_Off;
    }

    public void setDsl_lookup_media_off(boolean dsl_Lookup_Media_Off) {
        this.dsl_Lookup_Media_Off = dsl_Lookup_Media_Off;
    }
    public String getDsl_lookup_overrideday() {
        return dsl_Lookup_OverrideDay;
    }

    public void setDsl_lookup_overrideday(String dsl_Lookup_OverrideDay) {
        this.dsl_Lookup_OverrideDay = dsl_Lookup_OverrideDay;
    }
    public boolean getDsl_lookup_override_mode_set() {
        return dsl_Lookup_Override_Mode_Set;
    }

    public void setDsl_lookup_override_mode_set(boolean dsl_Lookup_Override_Mode_Set) {
        this.dsl_Lookup_Override_Mode_Set = dsl_Lookup_Override_Mode_Set;
    }
    public boolean getDsl_lookup_override__day_set() {
        return dsl_Lookup_Override__Day_Set;
    }

    public void setDsl_lookup_override__day_set(boolean dsl_Lookup_Override__Day_Set) {
        this.dsl_Lookup_Override__Day_Set = dsl_Lookup_Override__Day_Set;
    }
    public String getDsl_lookup_overridemode() {
        return dsl_Lookup_OverrideMode;
    }

    public void setDsl_lookup_overridemode(String dsl_Lookup_OverrideMode) {
        this.dsl_Lookup_OverrideMode = dsl_Lookup_OverrideMode;
    }


}