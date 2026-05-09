





import java.util.List;
import java.util.ArrayList;

public class rapidml_ResourceAPI extends RESTElement, HasTitle, HasSecurityValue {

    private String baseURI;
    private String name;
    private String version;





    private List<rapidml_MediaType> rapidml_mediatypes;




    private List<rapidml_ResourceDefinition> rapidml_resourcedefinitions;




    private List<rapidml_MediaType> rapidml_mediatypes;


    public rapidml_ResourceAPI(
        String baseURI,        String name,        String version    ) {
        super(
        );
        this.baseURI = baseURI;
        this.name = name;
        this.version = version;
        this.rapidml_mediatypes = new ArrayList<>();
        this.rapidml_resourcedefinitions = new ArrayList<>();
        this.rapidml_mediatypes = new ArrayList<>();
    }

    public rapidml_ResourceAPI(
        String baseURI,        String name,        String version        ArrayList<rapidml_MediaType> rapidml_mediatypes,        ArrayList<rapidml_ResourceDefinition> rapidml_resourcedefinitions,        ArrayList<rapidml_MediaType> rapidml_mediatypes    ) {
        this.baseURI = baseURI;
        this.name = name;
        this.version = version;
        this.rapidml_mediatypes = rapidml_mediatypes;
        this.rapidml_resourcedefinitions = rapidml_resourcedefinitions;
        this.rapidml_mediatypes = rapidml_mediatypes;
    }

    public String getBaseuri() {
        return baseURI;
    }

    public void setBaseuri(String baseURI) {
        this.baseURI = baseURI;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public List<rapidml_MediaType> getRapidml_mediatypes() {
        return rapidml_mediatypes;
    }

    public void addRapidml_mediatype(Rapidml_mediatype rapidml_mediatype) {
        this.rapidml_mediatypes.add(rapidml_mediatype);
    }
    public List<rapidml_ResourceDefinition> getRapidml_resourcedefinitions() {
        return rapidml_resourcedefinitions;
    }

    public void addRapidml_resourcedefinition(Rapidml_resourcedefinition rapidml_resourcedefinition) {
        this.rapidml_resourcedefinitions.add(rapidml_resourcedefinition);
    }
    public List<rapidml_MediaType> getRapidml_mediatypes() {
        return rapidml_mediatypes;
    }

    public void addRapidml_mediatype(Rapidml_mediatype rapidml_mediatype) {
        this.rapidml_mediatypes.add(rapidml_mediatype);
    }

}