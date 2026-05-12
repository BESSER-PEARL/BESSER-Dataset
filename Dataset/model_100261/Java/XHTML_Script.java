





import java.util.List;
import java.util.ArrayList;

public class XHTML_Script extends Miscinline, PCDATA, HeadMisc {

    private String defer;
    private String xml_space;





    private Charset charset;




    private URI uri;




    private ContentType contenttype;




    private ID id;


    public XHTML_Script(
        String defer,        String xml_space    ) {
        super(
        );
        this.defer = defer;
        this.xml_space = xml_space;
    }


    public String getDefer() {
        return defer;
    }

    public void setDefer(String defer) {
        this.defer = defer;
    }
    public String getXml_space() {
        return xml_space;
    }

    public void setXml_space(String xml_space) {
        this.xml_space = xml_space;
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
    public ID getId() {
        return id;
    }

    public void setId(ID id) {
        this.id = id;
    }

}