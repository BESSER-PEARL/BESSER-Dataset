





import java.util.List;
import java.util.ArrayList;

public class tExp_Constraint  {

    private String together;
    private String parMin;
    private String split;
    private String parMax;





    private List<tExp_Role> texp_roles;




    private List<tExp_Role> texp_roles;




    private tExp_TraceExpression texp_traceexpression;


    public tExp_Constraint(
        String together,        String parMin,        String split,        String parMax    ) {
        this.together = together;
        this.parMin = parMin;
        this.split = split;
        this.parMax = parMax;
        this.texp_roles = new ArrayList<>();
        this.texp_roles = new ArrayList<>();
    }

    public tExp_Constraint(
        String together,        String parMin,        String split,        String parMax        ArrayList<tExp_Role> texp_roles,        ArrayList<tExp_Role> texp_roles    ) {
        this.together = together;
        this.parMin = parMin;
        this.split = split;
        this.parMax = parMax;
        this.texp_roles = texp_roles;
        this.texp_roles = texp_roles;
    }

    public String getTogether() {
        return together;
    }

    public void setTogether(String together) {
        this.together = together;
    }
    public String getParmin() {
        return parMin;
    }

    public void setParmin(String parMin) {
        this.parMin = parMin;
    }
    public String getSplit() {
        return split;
    }

    public void setSplit(String split) {
        this.split = split;
    }
    public String getParmax() {
        return parMax;
    }

    public void setParmax(String parMax) {
        this.parMax = parMax;
    }

    public List<tExp_Role> getTexp_roles() {
        return texp_roles;
    }

    public void addTexp_role(Texp_role texp_role) {
        this.texp_roles.add(texp_role);
    }
    public List<tExp_Role> getTexp_roles() {
        return texp_roles;
    }

    public void addTexp_role(Texp_role texp_role) {
        this.texp_roles.add(texp_role);
    }
    public tExp_TraceExpression getTexp_traceexpression() {
        return texp_traceexpression;
    }

    public void setTexp_traceexpression(tExp_TraceExpression texp_traceexpression) {
        this.texp_traceexpression = texp_traceexpression;
    }

}