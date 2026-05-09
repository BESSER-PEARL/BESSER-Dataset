





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlOnexitType  {

    private String any;
    private String anyAttribute;
    private String scxmlCoreExecutablecontent;





    private scxml_ScxmlFinalType scxml_scxmlfinaltype;




    private List<scxml_ScxmlAssignType> scxml_scxmlassigntypes;




    private List<scxml_ScxmlCancelType> scxml_scxmlcanceltypes;




    private scxml_DocumentRoot scxml_documentroot;




    private List<scxml_ScxmlForeachType> scxml_scxmlforeachtypes;


    public scxml_ScxmlOnexitType(
        String any,        String anyAttribute,        String scxmlCoreExecutablecontent    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxml_scxmlassigntypes = new ArrayList<>();
        this.scxml_scxmlcanceltypes = new ArrayList<>();
        this.scxml_scxmlforeachtypes = new ArrayList<>();
    }

    public scxml_ScxmlOnexitType(
        String any,        String anyAttribute,        String scxmlCoreExecutablecontent        ArrayList<scxml_ScxmlAssignType> scxml_scxmlassigntypes,        ArrayList<scxml_ScxmlCancelType> scxml_scxmlcanceltypes,        ArrayList<scxml_ScxmlForeachType> scxml_scxmlforeachtypes    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxml_scxmlassigntypes = scxml_scxmlassigntypes;
        this.scxml_scxmlcanceltypes = scxml_scxmlcanceltypes;
        this.scxml_scxmlforeachtypes = scxml_scxmlforeachtypes;
    }

    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getScxmlcoreexecutablecontent() {
        return scxmlCoreExecutablecontent;
    }

    public void setScxmlcoreexecutablecontent(String scxmlCoreExecutablecontent) {
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
    }

    public scxml_ScxmlFinalType getScxml_scxmlfinaltype() {
        return scxml_scxmlfinaltype;
    }

    public void setScxml_scxmlfinaltype(scxml_ScxmlFinalType scxml_scxmlfinaltype) {
        this.scxml_scxmlfinaltype = scxml_scxmlfinaltype;
    }
    public List<scxml_ScxmlAssignType> getScxml_scxmlassigntypes() {
        return scxml_scxmlassigntypes;
    }

    public void addScxml_scxmlassigntype(Scxml_scxmlassigntype scxml_scxmlassigntype) {
        this.scxml_scxmlassigntypes.add(scxml_scxmlassigntype);
    }
    public List<scxml_ScxmlCancelType> getScxml_scxmlcanceltypes() {
        return scxml_scxmlcanceltypes;
    }

    public void addScxml_scxmlcanceltype(Scxml_scxmlcanceltype scxml_scxmlcanceltype) {
        this.scxml_scxmlcanceltypes.add(scxml_scxmlcanceltype);
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }
    public List<scxml_ScxmlForeachType> getScxml_scxmlforeachtypes() {
        return scxml_scxmlforeachtypes;
    }

    public void addScxml_scxmlforeachtype(Scxml_scxmlforeachtype scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtypes.add(scxml_scxmlforeachtype);
    }

}