





import java.util.List;
import java.util.ArrayList;

public class go_IfStmt  {






    private List<go_Block> go_blocks;




    private go_IfStmt go_ifstmt;




    private go_Expression go_expression;




    private go_Statement go_statement;


    public go_IfStmt(
    ) {
        this.go_blocks = new ArrayList<>();
    }

    public go_IfStmt(
        ArrayList<go_Block> go_blocks    ) {
        this.go_blocks = go_blocks;
    }


    public List<go_Block> getGo_blocks() {
        return go_blocks;
    }

    public void addGo_block(Go_block go_block) {
        this.go_blocks.add(go_block);
    }
    public go_IfStmt getGo_ifstmt() {
        return go_ifstmt;
    }

    public void setGo_ifstmt(go_IfStmt go_ifstmt) {
        this.go_ifstmt = go_ifstmt;
    }
    public go_Expression getGo_expression() {
        return go_expression;
    }

    public void setGo_expression(go_Expression go_expression) {
        this.go_expression = go_expression;
    }
    public go_Statement getGo_statement() {
        return go_statement;
    }

    public void setGo_statement(go_Statement go_statement) {
        this.go_statement = go_statement;
    }

}