





import java.util.List;
import java.util.ArrayList;

public class rapidml_RealizationModelLocation  {

    private String uri;





    private rapidml_ResourceAPI rapidml_resourceapi;


    public rapidml_RealizationModelLocation(
        String uri    ) {
        this.uri = uri;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public rapidml_ResourceAPI getRapidml_resourceapi() {
        return rapidml_resourceapi;
    }

    public void setRapidml_resourceapi(rapidml_ResourceAPI rapidml_resourceapi) {
        this.rapidml_resourceapi = rapidml_resourceapi;
    }

}