





import java.util.List;
import java.util.ArrayList;

public class java_Statement extends ASTNode {






    private java_LabeledStatement java_labeledstatement;




    private java_Block java_block;


    public java_Statement(
    ) {
        super(
        );
    }



    public java_LabeledStatement getJava_labeledstatement() {
        return java_labeledstatement;
    }

    public void setJava_labeledstatement(java_LabeledStatement java_labeledstatement) {
        this.java_labeledstatement = java_labeledstatement;
    }
    public java_Block getJava_block() {
        return java_block;
    }

    public void setJava_block(java_Block java_block) {
        this.java_block = java_block;
    }

}