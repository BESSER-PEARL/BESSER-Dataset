





import java.util.List;
import java.util.ArrayList;

public class cal_AstType  {

    private String builtin;





    private cal_AstTypeName cal_asttypename;




    private List<cal_AstType> cal_asttypes;




    private cal_AstFunction cal_astfunction;




    private cal_AstPort cal_astport;




    private List<cal_AstType> cal_asttypes;




    private List<cal_AstVariable> cal_astvariables;




    private List<cal_AstExpression> cal_astexpressions;




    private cal_AstTypeName cal_asttypename;




    private cal_AstVariable cal_astvariable;


    public cal_AstType(
        String builtin    ) {
        this.builtin = builtin;
        this.cal_asttypes = new ArrayList<>();
        this.cal_asttypes = new ArrayList<>();
        this.cal_astvariables = new ArrayList<>();
        this.cal_astexpressions = new ArrayList<>();
    }

    public cal_AstType(
        String builtin        ArrayList<cal_AstType> cal_asttypes,        ArrayList<cal_AstType> cal_asttypes,        ArrayList<cal_AstVariable> cal_astvariables,        ArrayList<cal_AstExpression> cal_astexpressions    ) {
        this.builtin = builtin;
        this.cal_asttypes = cal_asttypes;
        this.cal_asttypes = cal_asttypes;
        this.cal_astvariables = cal_astvariables;
        this.cal_astexpressions = cal_astexpressions;
    }

    public String getBuiltin() {
        return builtin;
    }

    public void setBuiltin(String builtin) {
        this.builtin = builtin;
    }

    public cal_AstTypeName getCal_asttypename() {
        return cal_asttypename;
    }

    public void setCal_asttypename(cal_AstTypeName cal_asttypename) {
        this.cal_asttypename = cal_asttypename;
    }
    public List<cal_AstType> getCal_asttypes() {
        return cal_asttypes;
    }

    public void addCal_asttype(Cal_asttype cal_asttype) {
        this.cal_asttypes.add(cal_asttype);
    }
    public cal_AstFunction getCal_astfunction() {
        return cal_astfunction;
    }

    public void setCal_astfunction(cal_AstFunction cal_astfunction) {
        this.cal_astfunction = cal_astfunction;
    }
    public cal_AstPort getCal_astport() {
        return cal_astport;
    }

    public void setCal_astport(cal_AstPort cal_astport) {
        this.cal_astport = cal_astport;
    }
    public List<cal_AstType> getCal_asttypes() {
        return cal_asttypes;
    }

    public void addCal_asttype(Cal_asttype cal_asttype) {
        this.cal_asttypes.add(cal_asttype);
    }
    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }
    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }
    public cal_AstTypeName getCal_asttypename() {
        return cal_asttypename;
    }

    public void setCal_asttypename(cal_AstTypeName cal_asttypename) {
        this.cal_asttypename = cal_asttypename;
    }
    public cal_AstVariable getCal_astvariable() {
        return cal_astvariable;
    }

    public void setCal_astvariable(cal_AstVariable cal_astvariable) {
        this.cal_astvariable = cal_astvariable;
    }

}