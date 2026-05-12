





import java.util.List;
import java.util.ArrayList;

public class build_command_VersionAdvice extends IAdvise {

    private String version;



    public build_command_VersionAdvice(
        String version    ) {
        super(
        );
        this.version = version;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}