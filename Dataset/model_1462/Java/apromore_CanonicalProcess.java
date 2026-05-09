





import java.util.List;
import java.util.ArrayList;

public class apromore_CanonicalProcess  {

    private String uri;
    private String author;
    private String version;



    public apromore_CanonicalProcess(
        String uri,        String author,        String version    ) {
        this.uri = uri;
        this.author = author;
        this.version = version;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}