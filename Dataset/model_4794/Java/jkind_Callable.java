





import java.util.List;
import java.util.ArrayList;

public class jkind_Callable  {

    private String name;





    private List<jkind_VariableGroup> jkind_variablegroups;




    private jkind_CallExpr jkind_callexpr;




    private List<jkind_VariableGroup> jkind_variablegroups;


    public jkind_Callable(
        String name    ) {
        this.name = name;
        this.jkind_variablegroups = new ArrayList<>();
        this.jkind_variablegroups = new ArrayList<>();
    }

    public jkind_Callable(
        String name        ArrayList<jkind_VariableGroup> jkind_variablegroups,        ArrayList<jkind_VariableGroup> jkind_variablegroups    ) {
        this.name = name;
        this.jkind_variablegroups = jkind_variablegroups;
        this.jkind_variablegroups = jkind_variablegroups;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<jkind_VariableGroup> getJkind_variablegroups() {
        return jkind_variablegroups;
    }

    public void addJkind_variablegroup(Jkind_variablegroup jkind_variablegroup) {
        this.jkind_variablegroups.add(jkind_variablegroup);
    }
    public jkind_CallExpr getJkind_callexpr() {
        return jkind_callexpr;
    }

    public void setJkind_callexpr(jkind_CallExpr jkind_callexpr) {
        this.jkind_callexpr = jkind_callexpr;
    }
    public List<jkind_VariableGroup> getJkind_variablegroups() {
        return jkind_variablegroups;
    }

    public void addJkind_variablegroup(Jkind_variablegroup jkind_variablegroup) {
        this.jkind_variablegroups.add(jkind_variablegroup);
    }

}