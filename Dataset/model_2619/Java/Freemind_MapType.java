





import java.util.List;
import java.util.ArrayList;

public class Freemind_MapType  {

    private String version;





    private Freemind_DocumentRoot freemind_documentroot;


    public Freemind_MapType(
        String version    ) {
        this.version = version;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public Freemind_DocumentRoot getFreemind_documentroot() {
        return freemind_documentroot;
    }

    public void setFreemind_documentroot(Freemind_DocumentRoot freemind_documentroot) {
        this.freemind_documentroot = freemind_documentroot;
    }

}