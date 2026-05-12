





import java.util.List;
import java.util.ArrayList;

public class XHTML_Link extends HeadMisc, Attrs, EMPTY {






    private ContentType contenttype;




    private Charset charset;




    private URI uri;




    private LanguageCode languagecode;


    public XHTML_Link(
    ) {
        super(
        );
    }



    public ContentType getContenttype() {
        return contenttype;
    }

    public void setContenttype(ContentType contenttype) {
        this.contenttype = contenttype;
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
    public LanguageCode getLanguagecode() {
        return languagecode;
    }

    public void setLanguagecode(LanguageCode languagecode) {
        this.languagecode = languagecode;
    }

}