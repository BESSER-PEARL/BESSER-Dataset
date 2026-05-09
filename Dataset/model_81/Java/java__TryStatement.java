





import java.util.List;
import java.util.ArrayList;

public class java__TryStatement extends Statement {






    private List<java__CatchClause> java__catchclauses;




    private java__Block java__block;




    private java__Block java__block;


    public java__TryStatement(
    ) {
        super(
        );
        this.java__catchclauses = new ArrayList<>();
    }

    public java__TryStatement(
        ArrayList<java__CatchClause> java__catchclauses    ) {
        this.java__catchclauses = java__catchclauses;
    }


    public List<java__CatchClause> getJava__catchclauses() {
        return java__catchclauses;
    }

    public void addJava__catchclause(Java__catchclause java__catchclause) {
        this.java__catchclauses.add(java__catchclause);
    }
    public java__Block getJava__block() {
        return java__block;
    }

    public void setJava__block(java__Block java__block) {
        this.java__block = java__block;
    }
    public java__Block getJava__block() {
        return java__block;
    }

    public void setJava__block(java__Block java__block) {
        this.java__block = java__block;
    }

}