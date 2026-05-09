





import java.util.List;
import java.util.ArrayList;

public class presentation_XMLDataProvider extends AbstractDataProvider {

    private String xPath;
    private String group1;





    private List<presentation_Document> presentation_documents;


    public presentation_XMLDataProvider(
        String xPath,        String group1    ) {
        super(
        );
        this.xPath = xPath;
        this.group1 = group1;
        this.presentation_documents = new ArrayList<>();
    }

    public presentation_XMLDataProvider(
        String xPath,        String group1        ArrayList<presentation_Document> presentation_documents    ) {
        this.xPath = xPath;
        this.group1 = group1;
        this.presentation_documents = presentation_documents;
    }

    public String getXpath() {
        return xPath;
    }

    public void setXpath(String xPath) {
        this.xPath = xPath;
    }
    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }

    public List<presentation_Document> getPresentation_documents() {
        return presentation_documents;
    }

    public void addPresentation_document(Presentation_document presentation_document) {
        this.presentation_documents.add(presentation_document);
    }

}