





import java.util.List;
import java.util.ArrayList;

public class atem_VersionSwitch extends AbstractComponent, InfoElementType, PrefaceElementType {

    private String dsl_VersionSwitch_flag;



    public atem_VersionSwitch(
        String dsl_VersionSwitch_flag    ) {
        super(
        );
        this.dsl_VersionSwitch_flag = dsl_VersionSwitch_flag;
    }


    public String getDsl_versionswitch_flag() {
        return dsl_VersionSwitch_flag;
    }

    public void setDsl_versionswitch_flag(String dsl_VersionSwitch_flag) {
        this.dsl_VersionSwitch_flag = dsl_VersionSwitch_flag;
    }


}