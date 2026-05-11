





import java.util.List;
import java.util.ArrayList;

public class application_Interface extends ConfigurableElement {

    private String frontEndCaching;
    private String urlSuffix;



    public application_Interface(
        String frontEndCaching,        String urlSuffix    ) {
        super(
        );
        this.frontEndCaching = frontEndCaching;
        this.urlSuffix = urlSuffix;
    }


    public String getFrontendcaching() {
        return frontEndCaching;
    }

    public void setFrontendcaching(String frontEndCaching) {
        this.frontEndCaching = frontEndCaching;
    }
    public String getUrlsuffix() {
        return urlSuffix;
    }

    public void setUrlsuffix(String urlSuffix) {
        this.urlSuffix = urlSuffix;
    }


}