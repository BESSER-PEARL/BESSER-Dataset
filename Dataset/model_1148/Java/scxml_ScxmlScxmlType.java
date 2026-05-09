





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlScxmlType  {

    private String any;
    private String name;
    private String anyAttribute;
    private String binding;
    private String datamodel1;
    private String initial;
    private String exmode;
    private String version;
    private String scxmlScxmlMix;





    private List<scxml_ScxmlFinalType> scxml_scxmlfinaltypes;




    private List<scxml_ScxmlParallelType> scxml_scxmlparalleltypes;




    private scxml_DocumentRoot scxml_documentroot;




    private List<scxml_ScxmlDatamodelType> scxml_scxmldatamodeltypes;




    private List<scxml_ScxmlScriptType> scxml_scxmlscripttypes;


    public scxml_ScxmlScxmlType(
        String any,        String name,        String anyAttribute,        String binding,        String datamodel1,        String initial,        String exmode,        String version,        String scxmlScxmlMix    ) {
        this.any = any;
        this.name = name;
        this.anyAttribute = anyAttribute;
        this.binding = binding;
        this.datamodel1 = datamodel1;
        this.initial = initial;
        this.exmode = exmode;
        this.version = version;
        this.scxmlScxmlMix = scxmlScxmlMix;
        this.scxml_scxmlfinaltypes = new ArrayList<>();
        this.scxml_scxmlparalleltypes = new ArrayList<>();
        this.scxml_scxmldatamodeltypes = new ArrayList<>();
        this.scxml_scxmlscripttypes = new ArrayList<>();
    }

    public scxml_ScxmlScxmlType(
        String any,        String name,        String anyAttribute,        String binding,        String datamodel1,        String initial,        String exmode,        String version,        String scxmlScxmlMix        ArrayList<scxml_ScxmlFinalType> scxml_scxmlfinaltypes,        ArrayList<scxml_ScxmlParallelType> scxml_scxmlparalleltypes,        ArrayList<scxml_ScxmlDatamodelType> scxml_scxmldatamodeltypes,        ArrayList<scxml_ScxmlScriptType> scxml_scxmlscripttypes    ) {
        this.any = any;
        this.name = name;
        this.anyAttribute = anyAttribute;
        this.binding = binding;
        this.datamodel1 = datamodel1;
        this.initial = initial;
        this.exmode = exmode;
        this.version = version;
        this.scxmlScxmlMix = scxmlScxmlMix;
        this.scxml_scxmlfinaltypes = scxml_scxmlfinaltypes;
        this.scxml_scxmlparalleltypes = scxml_scxmlparalleltypes;
        this.scxml_scxmldatamodeltypes = scxml_scxmldatamodeltypes;
        this.scxml_scxmlscripttypes = scxml_scxmlscripttypes;
    }

    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getBinding() {
        return binding;
    }

    public void setBinding(String binding) {
        this.binding = binding;
    }
    public String getDatamodel1() {
        return datamodel1;
    }

    public void setDatamodel1(String datamodel1) {
        this.datamodel1 = datamodel1;
    }
    public String getInitial() {
        return initial;
    }

    public void setInitial(String initial) {
        this.initial = initial;
    }
    public String getExmode() {
        return exmode;
    }

    public void setExmode(String exmode) {
        this.exmode = exmode;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getScxmlscxmlmix() {
        return scxmlScxmlMix;
    }

    public void setScxmlscxmlmix(String scxmlScxmlMix) {
        this.scxmlScxmlMix = scxmlScxmlMix;
    }

    public List<scxml_ScxmlFinalType> getScxml_scxmlfinaltypes() {
        return scxml_scxmlfinaltypes;
    }

    public void addScxml_scxmlfinaltype(Scxml_scxmlfinaltype scxml_scxmlfinaltype) {
        this.scxml_scxmlfinaltypes.add(scxml_scxmlfinaltype);
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
    public List<scxml_ScxmlScriptType> getScxml_scxmlscripttypes() {
        return scxml_scxmlscripttypes;
    }

    public void addScxml_scxmlscripttype(Scxml_scxmlscripttype scxml_scxmlscripttype) {
        this.scxml_scxmlscripttypes.add(scxml_scxmlscripttype);
    }

}