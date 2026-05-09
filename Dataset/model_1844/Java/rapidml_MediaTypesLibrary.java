





import java.util.List;
import java.util.ArrayList;

public class rapidml_MediaTypesLibrary  {






    private rapidml_ZenModel rapidml_zenmodel;




    private List<rapidml_MediaType> rapidml_mediatypes;


    public rapidml_MediaTypesLibrary(
    ) {
        this.rapidml_mediatypes = new ArrayList<>();
    }

    public rapidml_MediaTypesLibrary(
        ArrayList<rapidml_MediaType> rapidml_mediatypes    ) {
        this.rapidml_mediatypes = rapidml_mediatypes;
    }


    public rapidml_ZenModel getRapidml_zenmodel() {
        return rapidml_zenmodel;
    }

    public void setRapidml_zenmodel(rapidml_ZenModel rapidml_zenmodel) {
        this.rapidml_zenmodel = rapidml_zenmodel;
    }
    public List<rapidml_MediaType> getRapidml_mediatypes() {
        return rapidml_mediatypes;
    }

    public void addRapidml_mediatype(Rapidml_mediatype rapidml_mediatype) {
        this.rapidml_mediatypes.add(rapidml_mediatype);
    }

}