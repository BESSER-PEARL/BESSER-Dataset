





import java.util.List;
import java.util.ArrayList;

public class gDSL_Val extends Decl {

    private String name;
    private String mid;
    private String attr;
    private String decPat;





    private gDSL_DeclExport gdsl_declexport;


    public gDSL_Val(
        String name,        String mid,        String attr,        String decPat    ) {
        super(
        );
        this.name = name;
        this.mid = mid;
        this.attr = attr;
        this.decPat = decPat;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMid() {
        return mid;
    }

    public void setMid(String mid) {
        this.mid = mid;
    }
    public String getAttr() {
        return attr;
    }

    public void setAttr(String attr) {
        this.attr = attr;
    }
    public String getDecpat() {
        return decPat;
    }

    public void setDecpat(String decPat) {
        this.decPat = decPat;
    }

    public gDSL_DeclExport getGdsl_declexport() {
        return gdsl_declexport;
    }

    public void setGdsl_declexport(gDSL_DeclExport gdsl_declexport) {
        this.gdsl_declexport = gdsl_declexport;
    }

}