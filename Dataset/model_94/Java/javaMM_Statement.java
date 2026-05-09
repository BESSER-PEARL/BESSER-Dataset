





import java.util.List;
import java.util.ArrayList;

public class javaMM_Statement extends ASTNode {






    private javaMM_WhileStatement javamm_whilestatement;




    private javaMM_Block javamm_block;




    private javaMM_SwitchStatement javamm_switchstatement;


    public javaMM_Statement(
    ) {
        super(
        );
    }



    public javaMM_WhileStatement getJavamm_whilestatement() {
        return javamm_whilestatement;
    }

    public void setJavamm_whilestatement(javaMM_WhileStatement javamm_whilestatement) {
        this.javamm_whilestatement = javamm_whilestatement;
    }
    public javaMM_Block getJavamm_block() {
        return javamm_block;
    }

    public void setJavamm_block(javaMM_Block javamm_block) {
        this.javamm_block = javamm_block;
    }
    public javaMM_SwitchStatement getJavamm_switchstatement() {
        return javamm_switchstatement;
    }

    public void setJavamm_switchstatement(javaMM_SwitchStatement javamm_switchstatement) {
        this.javamm_switchstatement = javamm_switchstatement;
    }

}