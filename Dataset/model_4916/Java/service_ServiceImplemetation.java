





import java.util.List;
import java.util.ArrayList;

public class service_ServiceImplemetation  {

    private String language;
    private String uri;



    public service_ServiceImplemetation(
        String language,        String uri    ) {
        this.language = language;
        this.uri = uri;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}