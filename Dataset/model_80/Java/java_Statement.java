





import java.util.List;
import java.util.ArrayList;

public class java_Statement extends ASTNode {






    private java_Block java_block;




    private java_WhileStatement java_whilestatement;


    public java_Statement(
    ) {
        super(
        );
    }



    public java_Block getJava_block() {
        return java_block;
    }

    public void setJava_block(java_Block java_block) {
        this.java_block = java_block;
    }
    public java_WhileStatement getJava_whilestatement() {
        return java_whilestatement;
    }

    public void setJava_whilestatement(java_WhileStatement java_whilestatement) {
        this.java_whilestatement = java_whilestatement;
    }

}