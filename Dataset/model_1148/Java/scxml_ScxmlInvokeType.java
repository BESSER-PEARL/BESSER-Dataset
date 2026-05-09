





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlInvokeType  {

    private String any;
    private String autoforward;
    private String scxmlInvokeMix;
    private String id;
    private String src;
    private String anyAttribute;
    private String type;
    private String srcexpr;
    private String namelist;
    private String typeexpr;
    private String idlocation;





    private List<scxml_ScxmlParamType> scxml_scxmlparamtypes;




    private scxml_DocumentRoot scxml_documentroot;




    private List<scxml_ScxmlFinalizeType> scxml_scxmlfinalizetypes;




    private List<scxml_ScxmlContentType> scxml_scxmlcontenttypes;




    private scxml_ScxmlParallelType scxml_scxmlparalleltype;


    public scxml_ScxmlInvokeType(
        String any,        String autoforward,        String scxmlInvokeMix,        String id,        String src,        String anyAttribute,        String type,        String srcexpr,        String namelist,        String typeexpr,        String idlocation    ) {
        this.any = any;
        this.autoforward = autoforward;
        this.scxmlInvokeMix = scxmlInvokeMix;
        this.id = id;
        this.src = src;
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.srcexpr = srcexpr;
        this.namelist = namelist;
        this.typeexpr = typeexpr;
        this.idlocation = idlocation;
        this.scxml_scxmlparamtypes = new ArrayList<>();
        this.scxml_scxmlfinalizetypes = new ArrayList<>();
        this.scxml_scxmlcontenttypes = new ArrayList<>();
    }

    public scxml_ScxmlInvokeType(
        String any,        String autoforward,        String scxmlInvokeMix,        String id,        String src,        String anyAttribute,        String type,        String srcexpr,        String namelist,        String typeexpr,        String idlocation        ArrayList<scxml_ScxmlParamType> scxml_scxmlparamtypes,        ArrayList<scxml_ScxmlFinalizeType> scxml_scxmlfinalizetypes,        ArrayList<scxml_ScxmlContentType> scxml_scxmlcontenttypes    ) {
        this.any = any;
        this.autoforward = autoforward;
        this.scxmlInvokeMix = scxmlInvokeMix;
        this.id = id;
        this.src = src;
        this.anyAttribute = anyAttribute;
        this.type = type;
        this.srcexpr = srcexpr;
        this.namelist = namelist;
        this.typeexpr = typeexpr;
        this.idlocation = idlocation;
        this.scxml_scxmlparamtypes = scxml_scxmlparamtypes;
        this.scxml_scxmlfinalizetypes = scxml_scxmlfinalizetypes;
        this.scxml_scxmlcontenttypes = scxml_scxmlcontenttypes;
    }

    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getAutoforward() {
        return autoforward;
    }

    public void setAutoforward(String autoforward) {
        this.autoforward = autoforward;
    }
    public String getScxmlinvokemix() {
        return scxmlInvokeMix;
    }

    public void setScxmlinvokemix(String scxmlInvokeMix) {
        this.scxmlInvokeMix = scxmlInvokeMix;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSrcexpr() {
        return srcexpr;
    }

    public void setSrcexpr(String srcexpr) {
        this.srcexpr = srcexpr;
    }
    public String getNamelist() {
        return namelist;
    }

    public void setNamelist(String namelist) {
        this.namelist = namelist;
    }
    public String getTypeexpr() {
        return typeexpr;
    }

    public void setTypeexpr(String typeexpr) {
        this.typeexpr = typeexpr;
    }
    public String getIdlocation() {
        return idlocation;
    }

    public void setIdlocation(String idlocation) {
        this.idlocation = idlocation;
    }

    public List<scxml_ScxmlParamType> getScxml_scxmlparamtypes() {
        return scxml_scxmlparamtypes;
    }

    public void addScxml_scxmlparamtype(Scxml_scxmlparamtype scxml_scxmlparamtype) {
        this.scxml_scxmlparamtypes.add(scxml_scxmlparamtype);
    }
    public scxml_DocumentRoot getScxml_documentroot() {
        return scxml_documentroot;
    }

    public void setScxml_documentroot(scxml_DocumentRoot scxml_documentroot) {
        this.scxml_documentroot = scxml_documentroot;
    }
    public List<scxml_ScxmlFinalizeType> getScxml_scxmlfinalizetypes() {
        return scxml_scxmlfinalizetypes;
    }

    public void addScxml_scxmlfinalizetype(Scxml_scxmlfinalizetype scxml_scxmlfinalizetype) {
        this.scxml_scxmlfinalizetypes.add(scxml_scxmlfinalizetype);
    }
    public List<scxml_ScxmlContentType> getScxml_scxmlcontenttypes() {
        return scxml_scxmlcontenttypes;
    }

    public void addScxml_scxmlcontenttype(Scxml_scxmlcontenttype scxml_scxmlcontenttype) {
        this.scxml_scxmlcontenttypes.add(scxml_scxmlcontenttype);
    }
    public scxml_ScxmlParallelType getScxml_scxmlparalleltype() {
        return scxml_scxmlparalleltype;
    }

    public void setScxml_scxmlparalleltype(scxml_ScxmlParallelType scxml_scxmlparalleltype) {
        this.scxml_scxmlparalleltype = scxml_scxmlparalleltype;
    }

}