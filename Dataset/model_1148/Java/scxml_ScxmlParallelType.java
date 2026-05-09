





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlParallelType  {

    private String anyAttribute;
    private String scxmlParallelMix;
    private String id;
    private String any;





    private List<scxml_ScxmlOnexitType> scxml_scxmlonexittypes;




    private List<scxml_ScxmlOnentryType> scxml_scxmlonentrytypes;




    private List<scxml_ScxmlParallelType> scxml_scxmlparalleltypes;




    private scxml_DocumentRoot scxml_documentroot;




    private List<scxml_ScxmlDatamodelType> scxml_scxmldatamodeltypes;


    public scxml_ScxmlParallelType(
        String anyAttribute,        String scxmlParallelMix,        String id,        String any    ) {
        this.anyAttribute = anyAttribute;
        this.scxmlParallelMix = scxmlParallelMix;
        this.id = id;
        this.any = any;
        this.scxml_scxmlonexittypes = new ArrayList<>();
        this.scxml_scxmlonentrytypes = new ArrayList<>();
        this.scxml_scxmlparalleltypes = new ArrayList<>();
        this.scxml_scxmldatamodeltypes = new ArrayList<>();
    }

    public scxml_ScxmlParallelType(
        String anyAttribute,        String scxmlParallelMix,        String id,        String any        ArrayList<scxml_ScxmlOnexitType> scxml_scxmlonexittypes,        ArrayList<scxml_ScxmlOnentryType> scxml_scxmlonentrytypes,        ArrayList<scxml_ScxmlParallelType> scxml_scxmlparalleltypes,        ArrayList<scxml_ScxmlDatamodelType> scxml_scxmldatamodeltypes    ) {
        this.anyAttribute = anyAttribute;
        this.scxmlParallelMix = scxmlParallelMix;
        this.id = id;
        this.any = any;
        this.scxml_scxmlonexittypes = scxml_scxmlonexittypes;
        this.scxml_scxmlonentrytypes = scxml_scxmlonentrytypes;
        this.scxml_scxmlparalleltypes = scxml_scxmlparalleltypes;
        this.scxml_scxmldatamodeltypes = scxml_scxmldatamodeltypes;
    }

    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getScxmlparallelmix() {
        return scxmlParallelMix;
    }

    public void setScxmlparallelmix(String scxmlParallelMix) {
        this.scxmlParallelMix = scxmlParallelMix;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }

    public List<scxml_ScxmlOnexitType> getScxml_scxmlonexittypes() {
        return scxml_scxmlonexittypes;
    }

    public void addScxml_scxmlonexittype(Scxml_scxmlonexittype scxml_scxmlonexittype) {
        this.scxml_scxmlonexittypes.add(scxml_scxmlonexittype);
    }
    public List<scxml_ScxmlOnentryType> getScxml_scxmlonentrytypes() {
        return scxml_scxmlonentrytypes;
    }

    public void addScxml_scxmlonentrytype(Scxml_scxmlonentrytype scxml_scxmlonentrytype) {
        this.scxml_scxmlonentrytypes.add(scxml_scxmlonentrytype);
    }
    public List<scxml_ScxmlParallelType> getScxml_scxmlparalleltypes() {
        return scxml_scxmlparalleltypes;
    }

    public void addScxml_scxmlparalleltype(Scxml_scxmlparalleltype scxml_scxmlparalleltype) {
        this.scxml_scxmlparalleltypes.add(scxml_scxmlparalleltype);
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }
    public List<scxml_ScxmlDatamodelType> getScxml_scxmldatamodeltypes() {
        return scxml_scxmldatamodeltypes;
    }

    public void addScxml_scxmldatamodeltype(Scxml_scxmldatamodeltype scxml_scxmldatamodeltype) {
        this.scxml_scxmldatamodeltypes.add(scxml_scxmldatamodeltype);
    }

}