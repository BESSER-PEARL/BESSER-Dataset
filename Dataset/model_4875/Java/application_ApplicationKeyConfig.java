





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationKeyConfig extends Security {

    private String applicationKeys;



    public application_ApplicationKeyConfig(
        String applicationKeys    ) {
        super(
        );
        this.applicationKeys = applicationKeys;
    }


    public String getApplicationkeys() {
        return applicationKeys;
    }

    public void setApplicationkeys(String applicationKeys) {
        this.applicationKeys = applicationKeys;
    }


}