





import java.util.List;
import java.util.ArrayList;

public class rapidml_ImportDeclaration  {

    private String importedNamespace;
    private String alias;
    private String importURI;





    private rapidml_ZenModel rapidml_zenmodel;




    private rapidml_ZenModel rapidml_zenmodel;


    public rapidml_ImportDeclaration(
        String importedNamespace,        String alias,        String importURI    ) {
        this.importedNamespace = importedNamespace;
        this.alias = alias;
        this.importURI = importURI;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
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

    public rapidml_ZenModel getRapidml_zenmodel() {
        return rapidml_zenmodel;
    }

    public void setRapidml_zenmodel(rapidml_ZenModel rapidml_zenmodel) {
        this.rapidml_zenmodel = rapidml_zenmodel;
    }
    public rapidml_ZenModel getRapidml_zenmodel() {
        return rapidml_zenmodel;
    }

    public void setRapidml_zenmodel(rapidml_ZenModel rapidml_zenmodel) {
        this.rapidml_zenmodel = rapidml_zenmodel;
    }

}