





import java.util.List;
import java.util.ArrayList;

public class nuSMV_SimpleExpression  {






    private nuSMV_DefineBody nusmv_definebody;




    private nuSMV_TransConstraint nusmv_transconstraint;




    private nuSMV_InvarConstraint nusmv_invarconstraint;




    private nuSMV_InitConstraint nusmv_initconstraint;


    public nuSMV_SimpleExpression(
    ) {
    }



    public nuSMV_DefineBody getNusmv_definebody() {
        return nusmv_definebody;
    }

    public void setNusmv_definebody(nuSMV_DefineBody nusmv_definebody) {
        this.nusmv_definebody = nusmv_definebody;
    }
    public nuSMV_TransConstraint getNusmv_transconstraint() {
        return nusmv_transconstraint;
    }

    public void setNusmv_transconstraint(nuSMV_TransConstraint nusmv_transconstraint) {
        this.nusmv_transconstraint = nusmv_transconstraint;
    }
    public nuSMV_InvarConstraint getNusmv_invarconstraint() {
        return nusmv_invarconstraint;
    }

    public void setNusmv_invarconstraint(nuSMV_InvarConstraint nusmv_invarconstraint) {
        this.nusmv_invarconstraint = nusmv_invarconstraint;
    }
    public nuSMV_InitConstraint getNusmv_initconstraint() {
        return nusmv_initconstraint;
    }

    public void setNusmv_initconstraint(nuSMV_InitConstraint nusmv_initconstraint) {
        this.nusmv_initconstraint = nusmv_initconstraint;
    }

}