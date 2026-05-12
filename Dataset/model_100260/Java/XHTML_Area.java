





import java.util.List;
import java.util.ArrayList;

public class XHTML_Area extends Focus, Attrs, EMPTY, MapElement {

    private String shape;
    private String nohref;





    private Text text;




    private URI uri;


    public XHTML_Area(
        String shape,        String nohref    ) {
        super(
        );
        this.shape = shape;
        this.nohref = nohref;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getNohref() {
        return nohref;
    }

    public void setNohref(String nohref) {
        this.nohref = nohref;
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

}