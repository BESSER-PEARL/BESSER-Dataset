





import java.util.List;
import java.util.ArrayList;

public class rapidml_LinkRelation extends Documentable {

    private String specURL;
    private String name;





    private rapidml_ResourceAPI rapidml_resourceapi;


    public rapidml_LinkRelation(
        String specURL,        String name    ) {
        super(
        );
        this.specURL = specURL;
        this.name = name;
    }


    public String getSpecurl() {
        return specURL;
    }

    public void setSpecurl(String specURL) {
        this.specURL = specURL;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rapidml_ResourceAPI getRapidml_resourceapi() {
        return rapidml_resourceapi;
    }

    public void setRapidml_resourceapi(rapidml_ResourceAPI rapidml_resourceapi) {
        this.rapidml_resourceapi = rapidml_resourceapi;
    }

}