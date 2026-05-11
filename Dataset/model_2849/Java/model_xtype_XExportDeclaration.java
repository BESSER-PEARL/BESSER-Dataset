





import java.util.List;
import java.util.ArrayList;

public class model_xtype_XExportDeclaration  {

    private String alias;
    private String importURI;
    private boolean wildcard;



    public model_xtype_XExportDeclaration(
        String alias,        String importURI,        boolean wildcard    ) {
        this.alias = alias;
        this.importURI = importURI;
        this.wildcard = wildcard;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }
    public boolean getWildcard() {
        return wildcard;
    }

    public void setWildcard(boolean wildcard) {
        this.wildcard = wildcard;
    }


}