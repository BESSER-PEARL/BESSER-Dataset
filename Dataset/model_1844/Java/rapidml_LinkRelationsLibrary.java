





import java.util.List;
import java.util.ArrayList;

public class rapidml_LinkRelationsLibrary  {

    private String name;





    private rapidml_ZenModel rapidml_zenmodel;




    private List<rapidml_LinkRelation> rapidml_linkrelations;


    public rapidml_LinkRelationsLibrary(
        String name    ) {
        this.name = name;
        this.rapidml_linkrelations = new ArrayList<>();
    }

    public rapidml_LinkRelationsLibrary(
        String name        ArrayList<rapidml_LinkRelation> rapidml_linkrelations    ) {
        this.name = name;
        this.rapidml_linkrelations = rapidml_linkrelations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rapidml_ZenModel getRapidml_zenmodel() {
        return rapidml_zenmodel;
    }

    public void setRapidml_zenmodel(rapidml_ZenModel rapidml_zenmodel) {
        this.rapidml_zenmodel = rapidml_zenmodel;
    }
    public List<rapidml_LinkRelation> getRapidml_linkrelations() {
        return rapidml_linkrelations;
    }

    public void addRapidml_linkrelation(Rapidml_linkrelation rapidml_linkrelation) {
        this.rapidml_linkrelations.add(rapidml_linkrelation);
    }

}