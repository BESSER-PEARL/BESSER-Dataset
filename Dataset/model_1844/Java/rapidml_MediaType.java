





import java.util.List;
import java.util.ArrayList;

public class rapidml_MediaType extends RESTElement {

    private String name;
    private String specURL;





    private rapidml_ResourceDefinition rapidml_resourcedefinition;




    private List<rapidml_MediaType> rapidml_mediatypes;




    private rapidml_ResourceDefinition rapidml_resourcedefinition;




    private rapidml_TypedMessage rapidml_typedmessage;


    public rapidml_MediaType(
        String name,        String specURL    ) {
        super(
        );
        this.name = name;
        this.specURL = specURL;
        this.rapidml_mediatypes = new ArrayList<>();
    }

    public rapidml_MediaType(
        String name,        String specURL        ArrayList<rapidml_MediaType> rapidml_mediatypes    ) {
        this.name = name;
        this.specURL = specURL;
        this.rapidml_mediatypes = rapidml_mediatypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSpecurl() {
        return specURL;
    }

    public void setSpecurl(String specURL) {
        this.specURL = specURL;
    }

    public rapidml_ResourceDefinition getRapidml_resourcedefinition() {
        return rapidml_resourcedefinition;
    }

    public void setRapidml_resourcedefinition(rapidml_ResourceDefinition rapidml_resourcedefinition) {
        this.rapidml_resourcedefinition = rapidml_resourcedefinition;
    }
    public List<rapidml_MediaType> getRapidml_mediatypes() {
        return rapidml_mediatypes;
    }

    public void addRapidml_mediatype(Rapidml_mediatype rapidml_mediatype) {
        this.rapidml_mediatypes.add(rapidml_mediatype);
    }
    public rapidml_ResourceDefinition getRapidml_resourcedefinition() {
        return rapidml_resourcedefinition;
    }

    public void setRapidml_resourcedefinition(rapidml_ResourceDefinition rapidml_resourcedefinition) {
        this.rapidml_resourcedefinition = rapidml_resourcedefinition;
    }
    public rapidml_TypedMessage getRapidml_typedmessage() {
        return rapidml_typedmessage;
    }

    public void setRapidml_typedmessage(rapidml_TypedMessage rapidml_typedmessage) {
        this.rapidml_typedmessage = rapidml_typedmessage;
    }

}