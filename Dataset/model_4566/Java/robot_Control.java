





import java.util.List;
import java.util.ArrayList;

public class robot_Control extends NamedElement {

    private String version;
    private int frameLimit;



    public robot_Control(
        String version,        int frameLimit    ) {
        super(
        );
        this.version = version;
        this.frameLimit = frameLimit;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public int getFramelimit() {
        return frameLimit;
    }

    public void setFramelimit(int frameLimit) {
        this.frameLimit = frameLimit;
    }


}