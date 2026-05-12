





import java.util.List;
import java.util.ArrayList;

public class XHTML_A extends Focus, Attrs, PreContent, inline {

    private String shape;





    private Charset charset;




    private URI uri;




    private ContentType contenttype;




    private LanguageCode languagecode;




    private NMTOKEN nmtoken;


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

    public Charset getCharset() {
        return charset;
    }

    public void setCharset(Charset charset) {
        this.charset = charset;
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
    public LanguageCode getLanguagecode() {
        return languagecode;
    }

    public void setLanguagecode(LanguageCode languagecode) {
        this.languagecode = languagecode;
    }
    public NMTOKEN getNmtoken() {
        return nmtoken;
    }

    public void setNmtoken(NMTOKEN nmtoken) {
        this.nmtoken = nmtoken;
    }

}