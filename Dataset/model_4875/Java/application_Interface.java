





import java.util.List;
import java.util.ArrayList;

public class application_Interface extends ConfigurableElement {

    private String urlSuffix;
    private String frontEndCaching;



    public application_Interface(
        String urlSuffix,        String frontEndCaching    ) {
        super(
        );
        this.urlSuffix = urlSuffix;
        this.frontEndCaching = frontEndCaching;
    }


    public String getUrlsuffix() {
        return urlSuffix;
    }

    public void setUrlsuffix(String urlSuffix) {
        this.urlSuffix = urlSuffix;
    }
    public String getFrontendcaching() {
        return frontEndCaching;
    }

    public void setFrontendcaching(String frontEndCaching) {
        this.frontEndCaching = frontEndCaching;
    }


}