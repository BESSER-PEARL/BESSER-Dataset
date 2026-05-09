





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlStateType  {

    private String any;
    private String anyAttribute;
    private String initial1;
    private String id;
    private String scxmlStateMix;





    private List<scxml_ScxmlDatamodelType> scxml_scxmldatamodeltypes;




    private List<scxml_ScxmlParallelType> scxml_scxmlparalleltypes;




    private List<scxml_ScxmlOnexitType> scxml_scxmlonexittypes;




    private List<scxml_ScxmlFinalType> scxml_scxmlfinaltypes;




    private List<scxml_ScxmlInvokeType> scxml_scxmlinvoketypes;




    private List<scxml_ScxmlInitialType> scxml_scxmlinitialtypes;




    private List<scxml_ScxmlStateType> scxml_scxmlstatetypes;




    private scxml_ScxmlScxmlType scxml_scxmlscxmltype;




    private List<scxml_ScxmlOnentryType> scxml_scxmlonentrytypes;




    private List<scxml_ScxmlHistoryType> scxml_scxmlhistorytypes;




    private scxml_DocumentRoot scxml_documentroot;




    private scxml_ScxmlParallelType scxml_scxmlparalleltype;


    public scxml_ScxmlStateType(
        String any,        String anyAttribute,        String initial1,        String id,        String scxmlStateMix    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.initial1 = initial1;
        this.id = id;
        this.scxmlStateMix = scxmlStateMix;
        this.scxml_scxmldatamodeltypes = new ArrayList<>();
        this.scxml_scxmlparalleltypes = new ArrayList<>();
        this.scxml_scxmlonexittypes = new ArrayList<>();
        this.scxml_scxmlfinaltypes = new ArrayList<>();
        this.scxml_scxmlinvoketypes = new ArrayList<>();
        this.scxml_scxmlinitialtypes = new ArrayList<>();
        this.scxml_scxmlstatetypes = new ArrayList<>();
        this.scxml_scxmlonentrytypes = new ArrayList<>();
        this.scxml_scxmlhistorytypes = new ArrayList<>();
    }

    public scxml_ScxmlStateType(
        String any,        String anyAttribute,        String initial1,        String id,        String scxmlStateMix        ArrayList<scxml_ScxmlDatamodelType> scxml_scxmldatamodeltypes,        ArrayList<scxml_ScxmlParallelType> scxml_scxmlparalleltypes,        ArrayList<scxml_ScxmlOnexitType> scxml_scxmlonexittypes,        ArrayList<scxml_ScxmlFinalType> scxml_scxmlfinaltypes,        ArrayList<scxml_ScxmlInvokeType> scxml_scxmlinvoketypes,        ArrayList<scxml_ScxmlInitialType> scxml_scxmlinitialtypes,        ArrayList<scxml_ScxmlStateType> scxml_scxmlstatetypes,        ArrayList<scxml_ScxmlOnentryType> scxml_scxmlonentrytypes,        ArrayList<scxml_ScxmlHistoryType> scxml_scxmlhistorytypes    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.initial1 = initial1;
        this.id = id;
        this.scxmlStateMix = scxmlStateMix;
        this.scxml_scxmldatamodeltypes = scxml_scxmldatamodeltypes;
        this.scxml_scxmlparalleltypes = scxml_scxmlparalleltypes;
        this.scxml_scxmlonexittypes = scxml_scxmlonexittypes;
        this.scxml_scxmlfinaltypes = scxml_scxmlfinaltypes;
        this.scxml_scxmlinvoketypes = scxml_scxmlinvoketypes;
        this.scxml_scxmlinitialtypes = scxml_scxmlinitialtypes;
        this.scxml_scxmlstatetypes = scxml_scxmlstatetypes;
        this.scxml_scxmlonentrytypes = scxml_scxmlonentrytypes;
        this.scxml_scxmlhistorytypes = scxml_scxmlhistorytypes;
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
    public String getInitial1() {
        return initial1;
    }

    public void setInitial1(String initial1) {
        this.initial1 = initial1;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getScxmlstatemix() {
        return scxmlStateMix;
    }

    public void setScxmlstatemix(String scxmlStateMix) {
        this.scxmlStateMix = scxmlStateMix;
    }

    public List<scxml_ScxmlDatamodelType> getScxml_scxmldatamodeltypes() {
        return scxml_scxmldatamodeltypes;
    }

    public void addScxml_scxmldatamodeltype(Scxml_scxmldatamodeltype scxml_scxmldatamodeltype) {
        this.scxml_scxmldatamodeltypes.add(scxml_scxmldatamodeltype);
    }
    public List<scxml_ScxmlParallelType> getScxml_scxmlparalleltypes() {
        return scxml_scxmlparalleltypes;
    }

    public void addScxml_scxmlparalleltype(Scxml_scxmlparalleltype scxml_scxmlparalleltype) {
        this.scxml_scxmlparalleltypes.add(scxml_scxmlparalleltype);
    }
    public List<scxml_ScxmlOnexitType> getScxml_scxmlonexittypes() {
        return scxml_scxmlonexittypes;
    }

    public void addScxml_scxmlonexittype(Scxml_scxmlonexittype scxml_scxmlonexittype) {
        this.scxml_scxmlonexittypes.add(scxml_scxmlonexittype);
    }
    public List<scxml_ScxmlFinalType> getScxml_scxmlfinaltypes() {
        return scxml_scxmlfinaltypes;
    }

    public void addScxml_scxmlfinaltype(Scxml_scxmlfinaltype scxml_scxmlfinaltype) {
        this.scxml_scxmlfinaltypes.add(scxml_scxmlfinaltype);
    }
    public List<scxml_ScxmlInvokeType> getScxml_scxmlinvoketypes() {
        return scxml_scxmlinvoketypes;
    }

    public void addScxml_scxmlinvoketype(Scxml_scxmlinvoketype scxml_scxmlinvoketype) {
        this.scxml_scxmlinvoketypes.add(scxml_scxmlinvoketype);
    }
    public List<scxml_ScxmlInitialType> getScxml_scxmlinitialtypes() {
        return scxml_scxmlinitialtypes;
    }

    public void addScxml_scxmlinitialtype(Scxml_scxmlinitialtype scxml_scxmlinitialtype) {
        this.scxml_scxmlinitialtypes.add(scxml_scxmlinitialtype);
    }
    public List<scxml_ScxmlStateType> getScxml_scxmlstatetypes() {
        return scxml_scxmlstatetypes;
    }

    public void addScxml_scxmlstatetype(Scxml_scxmlstatetype scxml_scxmlstatetype) {
        this.scxml_scxmlstatetypes.add(scxml_scxmlstatetype);
    }
    public scxml_ScxmlScxmlType getScxml_scxmlscxmltype() {
        return scxml_scxmlscxmltype;
    }

    public void setScxml_scxmlscxmltype(scxml_ScxmlScxmlType scxml_scxmlscxmltype) {
        this.scxml_scxmlscxmltype = scxml_scxmlscxmltype;
    }
    public List<scxml_ScxmlOnentryType> getScxml_scxmlonentrytypes() {
        return scxml_scxmlonentrytypes;
    }

    public void addScxml_scxmlonentrytype(Scxml_scxmlonentrytype scxml_scxmlonentrytype) {
        this.scxml_scxmlonentrytypes.add(scxml_scxmlonentrytype);
    }
    public List<scxml_ScxmlHistoryType> getScxml_scxmlhistorytypes() {
        return scxml_scxmlhistorytypes;
    }

    public void addScxml_scxmlhistorytype(Scxml_scxmlhistorytype scxml_scxmlhistorytype) {
        this.scxml_scxmlhistorytypes.add(scxml_scxmlhistorytype);
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }
    public scxml_ScxmlParallelType getScxml_scxmlparalleltype() {
        return scxml_scxmlparalleltype;
    }

    public void setScxml_scxmlparalleltype(scxml_ScxmlParallelType scxml_scxmlparalleltype) {
        this.scxml_scxmlparalleltype = scxml_scxmlparalleltype;
    }

}