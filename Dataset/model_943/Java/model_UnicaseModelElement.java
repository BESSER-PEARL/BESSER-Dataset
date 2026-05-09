





import java.util.List;
import java.util.ArrayList;

public class model_UnicaseModelElement extends ModelElement {

    private String description;
    private String state;
    private String name;





    private List<Annotation> annotations;




    private document_LeafSection document_leafsection;




    private List<Attachment> attachments;




    private List<document_LeafSection> document_leafsections;


    public model_UnicaseModelElement(
        String description,        String state,        String name    ) {
        super(
        );
        this.description = description;
        this.state = state;
        this.name = name;
        this.annotations = new ArrayList<>();
        this.attachments = new ArrayList<>();
        this.document_leafsections = new ArrayList<>();
    }

    public model_UnicaseModelElement(
        String description,        String state,        String name        ArrayList<Annotation> annotations,        ArrayList<Attachment> attachments,        ArrayList<document_LeafSection> document_leafsections    ) {
        this.description = description;
        this.state = state;
        this.name = name;
        this.annotations = annotations;
        this.attachments = attachments;
        this.document_leafsections = document_leafsections;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Annotation> getAnnotations() {
        return annotations;
    }

    public void addAnnotation(Annotation annotation) {
        this.annotations.add(annotation);
    }
    public document_LeafSection getDocument_leafsection() {
        return document_leafsection;
    }

    public void setDocument_leafsection(document_LeafSection document_leafsection) {
        this.document_leafsection = document_leafsection;
    }
    public List<Attachment> getAttachments() {
        return attachments;
    }

    public void addAttachment(Attachment attachment) {
        this.attachments.add(attachment);
    }
    public List<document_LeafSection> getDocument_leafsections() {
        return document_leafsections;
    }

    public void addDocument_leafsection(Document_leafsection document_leafsection) {
        this.document_leafsections.add(document_leafsection);
    }

}