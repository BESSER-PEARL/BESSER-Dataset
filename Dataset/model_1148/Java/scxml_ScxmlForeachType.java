





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlForeachType  {

    private String any;
    private String array;
    private String anyAttribute;
    private String index;
    private String scxmlCoreExecutablecontent;
    private String item;





    private List<scxml_ScxmlForeachType> scxml_scxmlforeachtypes;




    private List<scxml_ScxmlAssignType> scxml_scxmlassigntypes;




    private scxml_ScxmlFinalizeType scxml_scxmlfinalizetype;




    private scxml_DocumentRoot scxml_documentroot;


    public scxml_ScxmlForeachType(
        String any,        String array,        String anyAttribute,        String index,        String scxmlCoreExecutablecontent,        String item    ) {
        this.any = any;
        this.array = array;
        this.anyAttribute = anyAttribute;
        this.index = index;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.item = item;
        this.scxml_scxmlforeachtypes = new ArrayList<>();
        this.scxml_scxmlassigntypes = new ArrayList<>();
    }

    public scxml_ScxmlForeachType(
        String any,        String array,        String anyAttribute,        String index,        String scxmlCoreExecutablecontent,        String item        ArrayList<scxml_ScxmlForeachType> scxml_scxmlforeachtypes,        ArrayList<scxml_ScxmlAssignType> scxml_scxmlassigntypes    ) {
        this.any = any;
        this.array = array;
        this.anyAttribute = anyAttribute;
        this.index = index;
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
        this.item = item;
        this.scxml_scxmlforeachtypes = scxml_scxmlforeachtypes;
        this.scxml_scxmlassigntypes = scxml_scxmlassigntypes;
    }

    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getArray() {
        return array;
    }

    public void setArray(String array) {
        this.array = array;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getScxmlcoreexecutablecontent() {
        return scxmlCoreExecutablecontent;
    }

    public void setScxmlcoreexecutablecontent(String scxmlCoreExecutablecontent) {
        this.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent;
    }
    public String getItem() {
        return item;
    }

    public void setItem(String item) {
        this.item = item;
    }

    public List<scxml_ScxmlForeachType> getScxml_scxmlforeachtypes() {
        return scxml_scxmlforeachtypes;
    }

    public void addScxml_scxmlforeachtype(Scxml_scxmlforeachtype scxml_scxmlforeachtype) {
        this.scxml_scxmlforeachtypes.add(scxml_scxmlforeachtype);
    }
    public List<scxml_ScxmlAssignType> getScxml_scxmlassigntypes() {
        return scxml_scxmlassigntypes;
    }

    public void addScxml_scxmlassigntype(Scxml_scxmlassigntype scxml_scxmlassigntype) {
        this.scxml_scxmlassigntypes.add(scxml_scxmlassigntype);
    }
    public scxml_ScxmlFinalizeType getScxml_scxmlfinalizetype() {
        return scxml_scxmlfinalizetype;
    }

    public void setScxml_scxmlfinalizetype(scxml_ScxmlFinalizeType scxml_scxmlfinalizetype) {
        this.scxml_scxmlfinalizetype = scxml_scxmlfinalizetype;
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }

}