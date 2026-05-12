





import java.util.List;
import java.util.ArrayList;

public class XHTML_Object extends Special, Attrs, HeadMisc {

    private String declare;





    private Length length;




    private Text text;




    private URI uri;




    private URI uri;




    private ContentType contenttype;




    private ContentType contenttype;




    private NMTOKEN nmtoken;




    private Length length;




    private Number number;




    private List<ObjectElement> objectelements;




    private URI uri;




    private URI uri;


    public XHTML_Object(
        String declare    ) {
        super(
        );
        this.declare = declare;
        this.objectelements = new ArrayList<>();
    }

    public XHTML_Object(
        String declare        ArrayList<ObjectElement> objectelements    ) {
        this.declare = declare;
        this.objectelements = objectelements;
    }

    public String getDeclare() {
        return declare;
    }

    public void setDeclare(String declare) {
        this.declare = declare;
    }

    public Length getLength() {
        return length;
    }

    public void setLength(Length length) {
        this.length = length;
    }
    public Text getText() {
        return text;
    }

    public void setText(Text text) {
        this.text = text;
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }
    public ContentType getContenttype() {
        return contenttype;
    }

    public void setContenttype(ContentType contenttype) {
        this.contenttype = contenttype;
    }
    public ContentType getContenttype() {
        return contenttype;
    }

    public void setContenttype(ContentType contenttype) {
        this.contenttype = contenttype;
    }
    public NMTOKEN getNmtoken() {
        return nmtoken;
    }

    public void setNmtoken(NMTOKEN nmtoken) {
        this.nmtoken = nmtoken;
    }
    public Length getLength() {
        return length;
    }

    public void setLength(Length length) {
        this.length = length;
    }
    public Number getNumber() {
        return number;
    }

    public void setNumber(Number number) {
        this.number = number;
    }
    public List<ObjectElement> getObjectelements() {
        return objectelements;
    }

    public void addObjectelement(Objectelement objectelement) {
        this.objectelements.add(objectelement);
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }

}