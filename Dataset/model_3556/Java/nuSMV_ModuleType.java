





import java.util.List;
import java.util.ArrayList;

public class nuSMV_ModuleType extends Type {






    private nuSMV_VarBody nusmv_varbody;




    private List<nuSMV_SimpleExpression> nusmv_simpleexpressions;




    private nuSMV_Module nusmv_module;


    public nuSMV_ModuleType(
    ) {
        super(
        );
        this.nusmv_simpleexpressions = new ArrayList<>();
    }

    public nuSMV_ModuleType(
        ArrayList<nuSMV_SimpleExpression> nusmv_simpleexpressions    ) {
        this.nusmv_simpleexpressions = nusmv_simpleexpressions;
    }


    public nuSMV_VarBody getNusmv_varbody() {
        return nusmv_varbody;
    }

    public void setNusmv_varbody(nuSMV_VarBody nusmv_varbody) {
        this.nusmv_varbody = nusmv_varbody;
    }
    public List<nuSMV_SimpleExpression> getNusmv_simpleexpressions() {
        return nusmv_simpleexpressions;
    }

    public void addNusmv_simpleexpression(Nusmv_simpleexpression nusmv_simpleexpression) {
        this.nusmv_simpleexpressions.add(nusmv_simpleexpression);
    }
    public nuSMV_Module getNusmv_module() {
        return nusmv_module;
    }

    public void setNusmv_module(nuSMV_Module nusmv_module) {
        this.nusmv_module = nusmv_module;
    }

}