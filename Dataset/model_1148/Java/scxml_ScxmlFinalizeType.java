





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlFinalizeType  {

    private String any;
    private String anyAttribute;
    private String scxmlCoreExecutablecontent;





    private scxml_DocumentRoot scxml_documentroot;




    private List<scxml_ScxmlAssignType> scxml_scxmlassigntypes;


    public scxml_ScxmlFinalizeType(
        String any,        String anyAttribute,        String scxmlCoreExecutablecontent    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxml_scxmlassigntypes = new ArrayList<>();
    }

    public scxml_ScxmlFinalizeType(
        String any,        String anyAttribute,        String scxmlCoreExecutablecontent        ArrayList<scxml_ScxmlAssignType> scxml_scxmlassigntypes    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.scxml_scxmlassigntypes = scxml_scxmlassigntypes;
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

    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }
    public List<scxml_ScxmlAssignType> getScxml_scxmlassigntypes() {
        return scxml_scxmlassigntypes;
    }

    public void addScxml_scxmlassigntype(Scxml_scxmlassigntype scxml_scxmlassigntype) {
        this.scxml_scxmlassigntypes.add(scxml_scxmlassigntype);
    }

}