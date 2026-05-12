





import java.util.List;
import java.util.ArrayList;

public class XHTML_A extends Attrs, PreContent, Focus, inline {

    private String shape;





    private URI uri;




    private LanguageCode languagecode;




    private ContentType contenttype;




    private NMTOKEN nmtoken;




    private Charset charset;


    public XHTML_A(
        String shape    ) {
        super(
        );
        this.shape = shape;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }

    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }
    public LanguageCode getLanguagecode() {
        return languagecode;
    }

    public void setLanguagecode(LanguageCode languagecode) {
        this.languagecode = languagecode;
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
    public Charset getCharset() {
        return charset;
    }

    public void setCharset(Charset charset) {
        this.charset = charset;
    }

}