





import java.util.List;
import java.util.ArrayList;

public class reqSpec_ReqRoot  {

    private String title;
    private String issues;
    private String name;





    private List<reqSpec_ExternalDocument> reqspec_externaldocuments;




    private reqSpec_Description reqspec_description;


    public reqSpec_ReqRoot(
        String title,        String issues,        String name    ) {
        this.title = title;
        this.issues = issues;
        this.name = name;
        this.reqspec_externaldocuments = new ArrayList<>();
    }

    public reqSpec_ReqRoot(
        String title,        String issues,        String name        ArrayList<reqSpec_ExternalDocument> reqspec_externaldocuments    ) {
        this.title = title;
        this.issues = issues;
        this.name = name;
        this.reqspec_externaldocuments = reqspec_externaldocuments;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getIssues() {
        return issues;
    }

    public void setIssues(String issues) {
        this.issues = issues;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<reqSpec_ExternalDocument> getReqspec_externaldocuments() {
        return reqspec_externaldocuments;
    }

    public void addReqspec_externaldocument(Reqspec_externaldocument reqspec_externaldocument) {
        this.reqspec_externaldocuments.add(reqspec_externaldocument);
    }
    public reqSpec_Description getReqspec_description() {
        return reqspec_description;
    }

    public void setReqspec_description(reqSpec_Description reqspec_description) {
        this.reqspec_description = reqspec_description;
    }

}