





import java.util.List;
import java.util.ArrayList;

public class scxml_Invoke extends Donedata {

    private String namelist;
    private String typeexpr;
    private String type;
    private String idlocation;
    private String autoforward;
    private String srcexpr;
    private String id;
    private String src;





    private scxml_SimpleState scxml_simplestate;


    public scxml_Invoke(
        String namelist,        String typeexpr,        String type,        String idlocation,        String autoforward,        String srcexpr,        String id,        String src    ) {
        super(
        );
        this.namelist = namelist;
        this.typeexpr = typeexpr;
        this.type = type;
        this.idlocation = idlocation;
        this.autoforward = autoforward;
        this.srcexpr = srcexpr;
        this.id = id;
        this.src = src;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIdlocation() {
        return idlocation;
    }

    public void setIdlocation(String idlocation) {
        this.idlocation = idlocation;
    }
    public String getAutoforward() {
        return autoforward;
    }

    public void setAutoforward(String autoforward) {
        this.autoforward = autoforward;
    }
    public String getSrcexpr() {
        return srcexpr;
    }

    public void setSrcexpr(String srcexpr) {
        this.srcexpr = srcexpr;
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

    public scxml_SimpleState getScxml_simplestate() {
        return scxml_simplestate;
    }

    public void setScxml_simplestate(scxml_SimpleState scxml_simplestate) {
        this.scxml_simplestate = scxml_simplestate;
    }

}