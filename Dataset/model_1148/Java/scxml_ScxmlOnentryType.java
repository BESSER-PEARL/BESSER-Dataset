





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlOnentryType  {

    private String anyAttribute;
    private String any;
    private String scxmlCoreExecutablecontent;





    private List<scxml_ScxmlForeachType> scxml_scxmlforeachtypes;




    private scxml_ScxmlFinalType scxml_scxmlfinaltype;




    private scxml_DocumentRoot scxml_documentroot;




    private List<scxml_ScxmlCancelType> scxml_scxmlcanceltypes;




    private List<scxml_ScxmlAssignType> scxml_scxmlassigntypes;


    public scxml_ScxmlOnentryType(
        String anyAttribute,        String any,        String scxmlCoreExecutablecontent    ) {
        this.anyAttribute = anyAttribute;
        this.any = any;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxml_scxmlforeachtypes = new ArrayList<>();
        this.scxml_scxmlcanceltypes = new ArrayList<>();
        this.scxml_scxmlassigntypes = new ArrayList<>();
    }

    public scxml_ScxmlOnentryType(
        String anyAttribute,        String any,        String scxmlCoreExecutablecontent        ArrayList<scxml_ScxmlForeachType> scxml_scxmlforeachtypes,        ArrayList<scxml_ScxmlCancelType> scxml_scxmlcanceltypes,        ArrayList<scxml_ScxmlAssignType> scxml_scxmlassigntypes    ) {
        this.anyAttribute = anyAttribute;
        this.any = any;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxml_scxmlforeachtypes = scxml_scxmlforeachtypes;
        this.scxml_scxmlcanceltypes = scxml_scxmlcanceltypes;
        this.scxml_scxmlassigntypes = scxml_scxmlassigntypes;
    }

    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getScxmlcoreexecutablecontent() {
        return scxmlCoreExecutablecontent;
    }

    public void setScxmlcoreexecutablecontent(String scxmlCoreExecutablecontent) {
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
    }

    public List<scxml_ScxmlForeachType> getScxml_scxmlforeachtypes() {
        return scxml_scxmlforeachtypes;
    }

    public void addScxml_scxmlforeachtype(Scxml_scxmlforeachtype scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtypes.add(scxml_scxmlforeachtype);
    }
    public scxml_ScxmlFinalType getScxml_scxmlfinaltype() {
        return scxml_scxmlfinaltype;
    }

    public void setScxml_scxmlfinaltype(scxml_ScxmlFinalType scxml_scxmlfinaltype) {
        this.scxml_scxmlfinaltype = scxml_scxmlfinaltype;
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }
    public List<scxml_ScxmlCancelType> getScxml_scxmlcanceltypes() {
        return scxml_scxmlcanceltypes;
    }

    public void addScxml_scxmlcanceltype(Scxml_scxmlcanceltype scxml_scxmlcanceltype) {
        this.scxml_scxmlcanceltypes.add(scxml_scxmlcanceltype);
    }
    public List<scxml_ScxmlAssignType> getScxml_scxmlassigntypes() {
        return scxml_scxmlassigntypes;
    }

    public void addScxml_scxmlassigntype(Scxml_scxmlassigntype scxml_scxmlassigntype) {
        this.scxml_scxmlassigntypes.add(scxml_scxmlassigntype);
    }

}