





import java.util.List;
import java.util.ArrayList;

public class fl_DocumentRoot  {

    private String mixed;





    private List<fl_EStringToStringMapEntry> fl_estringtostringmapentrys;




    private List<fl_EStringToStringMapEntry> fl_estringtostringmapentrys;




    private List<fl_Expr> fl_exprs;




    private List<fl_ProgramType> fl_programtypes;


    public fl_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.fl_estringtostringmapentrys = new ArrayList<>();
        this.fl_estringtostringmapentrys = new ArrayList<>();
        this.fl_exprs = new ArrayList<>();
        this.fl_programtypes = new ArrayList<>();
    }

    public fl_DocumentRoot(
        String mixed        ArrayList<fl_EStringToStringMapEntry> fl_estringtostringmapentrys,        ArrayList<fl_EStringToStringMapEntry> fl_estringtostringmapentrys,        ArrayList<fl_Expr> fl_exprs,        ArrayList<fl_ProgramType> fl_programtypes    ) {
        this.mixed = mixed;
        this.fl_estringtostringmapentrys = fl_estringtostringmapentrys;
        this.fl_estringtostringmapentrys = fl_estringtostringmapentrys;
        this.fl_exprs = fl_exprs;
        this.fl_programtypes = fl_programtypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<fl_EStringToStringMapEntry> getFl_estringtostringmapentrys() {
        return fl_estringtostringmapentrys;
    }

    public void addFl_estringtostringmapentry(Fl_estringtostringmapentry fl_estringtostringmapentry) {
        this.fl_estringtostringmapentrys.add(fl_estringtostringmapentry);
    }
    public List<fl_EStringToStringMapEntry> getFl_estringtostringmapentrys() {
        return fl_estringtostringmapentrys;
    }

    public void addFl_estringtostringmapentry(Fl_estringtostringmapentry fl_estringtostringmapentry) {
        this.fl_estringtostringmapentrys.add(fl_estringtostringmapentry);
    }
    public List<fl_Expr> getFl_exprs() {
        return fl_exprs;
    }

    public void addFl_expr(Fl_expr fl_expr) {
        this.fl_exprs.add(fl_expr);
    }
    public List<fl_ProgramType> getFl_programtypes() {
        return fl_programtypes;
    }

    public void addFl_programtype(Fl_programtype fl_programtype) {
        this.fl_programtypes.add(fl_programtype);
    }

}