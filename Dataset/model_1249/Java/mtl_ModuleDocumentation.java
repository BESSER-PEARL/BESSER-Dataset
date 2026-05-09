





import java.util.List;
import java.util.ArrayList;

public class mtl_ModuleDocumentation extends Documentation {

    private String since;
    private String author;
    private String version;



    public mtl_ModuleDocumentation(
        String since,        String author,        String version    ) {
        super(
        );
        this.since = since;
        this.author = author;
        this.version = version;
    }


    public String getSince() {
        return since;
    }

    public void setSince(String since) {
        this.since = since;
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