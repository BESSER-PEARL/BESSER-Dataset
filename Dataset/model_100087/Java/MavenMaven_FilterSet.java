





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_FilterSet extends Set {

    private String endtoken;
    private String starttoken;



    public MavenMaven_FilterSet(
        String endtoken,        String starttoken    ) {
        super(
        );
        this.endtoken = endtoken;
        this.starttoken = starttoken;
    }


    public String getEndtoken() {
        return endtoken;
    }

    public void setEndtoken(String endtoken) {
        this.endtoken = endtoken;
    }
    public String getStarttoken() {
        return starttoken;
    }

    public void setStarttoken(String starttoken) {
        this.starttoken = starttoken;
    }


}