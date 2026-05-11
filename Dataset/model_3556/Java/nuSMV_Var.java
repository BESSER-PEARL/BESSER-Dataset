





import java.util.List;
import java.util.ArrayList;

public class nuSMV_Var extends SimpleExpression {






    private nuSMV_VarBody nusmv_varbody;




    private nuSMV_SimpleExpression nusmv_simpleexpression;


    public nuSMV_Var(
    ) {
        super(
        );
    }



    public nuSMV_VarBody getNusmv_varbody() {
        return nusmv_varbody;
    }

    public void setNusmv_varbody(nuSMV_VarBody nusmv_varbody) {
        this.nusmv_varbody = nusmv_varbody;
    }
    public nuSMV_SimpleExpression getNusmv_simpleexpression() {
        return nusmv_simpleexpression;
    }

    public void setNusmv_simpleexpression(nuSMV_SimpleExpression nusmv_simpleexpression) {
        this.nusmv_simpleexpression = nusmv_simpleexpression;
    }

}