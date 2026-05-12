





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_FilterSet extends Set {

    private String starttoken;
    private String endtoken;



    public MavenMaven_FilterSet(
        String starttoken,        String endtoken    ) {
        super(
        );
        this.starttoken = starttoken;
        this.endtoken = endtoken;
    }


    public String getStarttoken() {
        return starttoken;
    }

    public void setStarttoken(String starttoken) {
        this.starttoken = starttoken;
    }
    public String getEndtoken() {
        return endtoken;
    }

    public void setEndtoken(String endtoken) {
        this.endtoken = endtoken;
    }


}