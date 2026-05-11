





import java.util.List;
import java.util.ArrayList;

public class SecCon_UseCaseScenario extends NamedElement {

    private String author;
    private String version;



    public SecCon_UseCaseScenario(
        String author,        String version    ) {
        super(
        );
        this.author = author;
        this.version = version;
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