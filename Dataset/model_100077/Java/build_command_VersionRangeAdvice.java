





import java.util.List;
import java.util.ArrayList;

public class build_command_VersionRangeAdvice extends IAdvise {

    private String versionRange;



    public build_command_VersionRangeAdvice(
        String versionRange    ) {
        super(
        );
        this.versionRange = versionRange;
    }


    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
    }


}