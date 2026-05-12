





import java.util.List;
import java.util.ArrayList;

public class fsm_Expression  {






    private fsm_RelationalConstraint fsm_relationalconstraint;




    private fsm_VarDecl fsm_vardecl;




    private fsm_Assignation fsm_assignation;




    private fsm_Conditional fsm_conditional;




    private fsm_Loop fsm_loop;


    public fsm_Expression(
    ) {
    }



    public fsm_RelationalConstraint getFsm_relationalconstraint() {
        return fsm_relationalconstraint;
    }

    public void setFsm_relationalconstraint(fsm_RelationalConstraint fsm_relationalconstraint) {
        this.fsm_relationalconstraint = fsm_relationalconstraint;
    }
    public fsm_VarDecl getFsm_vardecl() {
        return fsm_vardecl;
    }

    public void setFsm_vardecl(fsm_VarDecl fsm_vardecl) {
        this.fsm_vardecl = fsm_vardecl;
    }
    public fsm_Assignation getFsm_assignation() {
        return fsm_assignation;
    }

    public void setFsm_assignation(fsm_Assignation fsm_assignation) {
        this.fsm_assignation = fsm_assignation;
    }
    public fsm_Conditional getFsm_conditional() {
        return fsm_conditional;
    }

    public void setFsm_conditional(fsm_Conditional fsm_conditional) {
        this.fsm_conditional = fsm_conditional;
    }
    public fsm_Loop getFsm_loop() {
        return fsm_loop;
    }

    public void setFsm_loop(fsm_Loop fsm_loop) {
        this.fsm_loop = fsm_loop;
    }

}