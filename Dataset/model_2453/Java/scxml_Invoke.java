





import java.util.List;
import java.util.ArrayList;

public class scxml_Invoke  {

    private String src;
    private String type;
    private String srcexpr;
    private String namelist;
    private String idlocation;
    private String typeexpr;
    private String autoforward;
    private String id;



    public scxml_Invoke(
        String src,        String type,        String srcexpr,        String namelist,        String idlocation,        String typeexpr,        String autoforward,        String id    ) {
        this.src = src;
        this.type = type;
        this.srcexpr = srcexpr;
        this.namelist = namelist;
        this.idlocation = idlocation;
        this.typeexpr = typeexpr;
        this.autoforward = autoforward;
        this.id = id;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
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
    public String getIdlocation() {
        return idlocation;
    }

    public void setIdlocation(String idlocation) {
        this.idlocation = idlocation;
    }
    public String getTypeexpr() {
        return typeexpr;
    }

    public void setTypeexpr(String typeexpr) {
        this.typeexpr = typeexpr;
    }
    public String getAutoforward() {
        return autoforward;
    }

    public void setAutoforward(String autoforward) {
        this.autoforward = autoforward;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}