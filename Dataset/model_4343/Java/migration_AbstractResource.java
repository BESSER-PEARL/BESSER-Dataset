





import java.util.List;
import java.util.ArrayList;

public class migration_AbstractResource  {

    private String uri;
    private String encoding;



    public migration_AbstractResource(
        String uri,        String encoding    ) {
        this.uri = uri;
        this.encoding = encoding;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }


}