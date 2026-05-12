





import java.util.List;
import java.util.ArrayList;

public class xwiki_XWiki extends LinkCollection {

    private String version;





    private xwiki_Syntaxes xwiki_syntaxes;


    public xwiki_XWiki(
        String version    ) {
        super(
        );
        this.version = version;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public xwiki_Syntaxes getXwiki_syntaxes() {
        return xwiki_syntaxes;
    }

    public void setXwiki_syntaxes(xwiki_Syntaxes xwiki_syntaxes) {
        this.xwiki_syntaxes = xwiki_syntaxes;
    }

}