





import java.util.List;
import java.util.ArrayList;

public class java_TryStatement extends Statement {






    private java_Block java_block;




    private java_Block java_block;




    private List<java_CatchClause> java_catchclauses;


    public java_TryStatement(
    ) {
        super(
        );
        this.java_catchclauses = new ArrayList<>();
    }

    public java_TryStatement(
        ArrayList<java_CatchClause> java_catchclauses    ) {
        this.java_catchclauses = java_catchclauses;
    }


    public java_Block getJava_block() {
        return java_block;
    }

    public void setJava_block(java_Block java_block) {
        this.java_block = java_block;
    }
    public java_Block getJava_block() {
        return java_block;
    }

    public void setJava_block(java_Block java_block) {
        this.java_block = java_block;
    }
    public List<java_CatchClause> getJava_catchclauses() {
        return java_catchclauses;
    }

    public void addJava_catchclause(Java_catchclause java_catchclause) {
        this.java_catchclauses.add(java_catchclause);
    }

}