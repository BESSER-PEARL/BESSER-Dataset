





import java.util.List;
import java.util.ArrayList;

public class assessment_Application extends Label, Notes {

    private String externalURL;
    private String internalURL;



    public assessment_Application(
        String externalURL,        String internalURL    ) {
        super(
        );
        this.externalURL = externalURL;
        this.internalURL = internalURL;
    }


    public String getExternalurl() {
        return externalURL;
    }

    public void setExternalurl(String externalURL) {
        this.externalURL = externalURL;
    }
    public String getInternalurl() {
        return internalURL;
    }

    public void setInternalurl(String internalURL) {
        this.internalURL = internalURL;
    }


}