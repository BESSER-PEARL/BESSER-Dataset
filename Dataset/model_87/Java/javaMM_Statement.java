





import java.util.List;
import java.util.ArrayList;

public class javaMM_Statement extends ASTNode {






    private javaMM_LabeledStatement javamm_labeledstatement;




    private javaMM_Block javamm_block;


    public javaMM_Statement(
    ) {
        super(
        );
    }



    public javaMM_LabeledStatement getJavamm_labeledstatement() {
        return javamm_labeledstatement;
    }

    public void setJavamm_labeledstatement(javaMM_LabeledStatement javamm_labeledstatement) {
        this.javamm_labeledstatement = javamm_labeledstatement;
    }
    public javaMM_Block getJavamm_block() {
        return javamm_block;
    }

    public void setJavamm_block(javaMM_Block javamm_block) {
        this.javamm_block = javamm_block;
    }

}