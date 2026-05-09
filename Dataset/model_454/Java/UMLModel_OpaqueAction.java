





import java.util.List;
import java.util.ArrayList;

public class UMLModel_OpaqueAction extends Action {

    private String language;
    private String body;





    private List<UMLModel_OutputPin> umlmodel_outputpins;


    public UMLModel_OpaqueAction(
        String language,        String body    ) {
        super(
        );
        this.language = language;
        this.body = body;
        this.umlmodel_outputpins = new ArrayList<>();
    }

    public UMLModel_OpaqueAction(
        String language,        String body        ArrayList<UMLModel_OutputPin> umlmodel_outputpins    ) {
        this.language = language;
        this.body = body;
        this.umlmodel_outputpins = umlmodel_outputpins;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public List<UMLModel_OutputPin> getUmlmodel_outputpins() {
        return umlmodel_outputpins;
    }

    public void addUmlmodel_outputpin(Umlmodel_outputpin umlmodel_outputpin) {
        this.umlmodel_outputpins.add(umlmodel_outputpin);
    }

}