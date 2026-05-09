





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Activity extends Behavior {

    private String language;
    private boolean isSingleExecution;
    private boolean isReadOnly;
    private String body;





    private List<UML2WithID_StructuredActivityNode> uml2withid_structuredactivitynodes;


    public UML2WithID_Activity(
        String language,        boolean isSingleExecution,        boolean isReadOnly,        String body    ) {
        super(
        );
        this.language = language;
        this.isSingleExecution = isSingleExecution;
        this.isReadOnly = isReadOnly;
        this.body = body;
        this.uml2withid_structuredactivitynodes = new ArrayList<>();
    }

    public UML2WithID_Activity(
        String language,        boolean isSingleExecution,        boolean isReadOnly,        String body        ArrayList<UML2WithID_StructuredActivityNode> uml2withid_structuredactivitynodes    ) {
        this.language = language;
        this.isSingleExecution = isSingleExecution;
        this.isReadOnly = isReadOnly;
        this.body = body;
        this.uml2withid_structuredactivitynodes = uml2withid_structuredactivitynodes;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public boolean getIssingleexecution() {
        return isSingleExecution;
    }

    public void setIssingleexecution(boolean isSingleExecution) {
        this.isSingleExecution = isSingleExecution;
    }
    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public List<UML2WithID_StructuredActivityNode> getUml2withid_structuredactivitynodes() {
        return uml2withid_structuredactivitynodes;
    }

    public void addUml2withid_structuredactivitynode(Uml2withid_structuredactivitynode uml2withid_structuredactivitynode) {
        this.uml2withid_structuredactivitynodes.add(uml2withid_structuredactivitynode);
    }

}