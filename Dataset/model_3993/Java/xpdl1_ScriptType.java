





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ScriptType  {

    private String grammar;
    private String version;
    private String type;





    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_PackageType xpdl1_packagetype;


    public xpdl1_ScriptType(
        String grammar,        String version,        String type    ) {
        this.grammar = grammar;
        this.version = version;
        this.type = type;
    }


    public String getGrammar() {
        return grammar;
    }

    public void setGrammar(String grammar) {
        this.grammar = grammar;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_PackageType getXpdl1_packagetype() {
        return xpdl1_packagetype;
    }

    public void setXpdl1_packagetype(xpdl1_PackageType xpdl1_packagetype) {
        this.xpdl1_packagetype = xpdl1_packagetype;
    }

}