





import java.util.List;
import java.util.ArrayList;

public class reqSpec_DocumentSection  {

    private String title;
    private String label;





    private List<reqSpec_EObject> reqspec_eobjects;




    private reqSpec_Description reqspec_description;


    public reqSpec_DocumentSection(
        String title,        String label    ) {
        this.title = title;
        this.label = label;
        this.reqspec_eobjects = new ArrayList<>();
    }

    public reqSpec_DocumentSection(
        String title,        String label        ArrayList<reqSpec_EObject> reqspec_eobjects    ) {
        this.title = title;
        this.label = label;
        this.reqspec_eobjects = reqspec_eobjects;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<reqSpec_EObject> getReqspec_eobjects() {
        return reqspec_eobjects;
    }

    public void addReqspec_eobject(Reqspec_eobject reqspec_eobject) {
        this.reqspec_eobjects.add(reqspec_eobject);
    }
    public reqSpec_Description getReqspec_description() {
        return reqspec_description;
    }

    public void setReqspec_description(reqSpec_Description reqspec_description) {
        this.reqspec_description = reqspec_description;
    }

}