





import java.util.List;
import java.util.ArrayList;

public class graph_Expr  {






    private graph_PrintStmt graph_printstmt;




    private graph_AssignStmt graph_assignstmt;




    private graph_IfStmt graph_ifstmt;




    private graph_WhileStmt graph_whilestmt;


    public graph_Expr(
    ) {
    }



    public graph_PrintStmt getGraph_printstmt() {
        return graph_printstmt;
    }

    public void setGraph_printstmt(graph_PrintStmt graph_printstmt) {
        this.graph_printstmt = graph_printstmt;
    }
    public graph_AssignStmt getGraph_assignstmt() {
        return graph_assignstmt;
    }

    public void setGraph_assignstmt(graph_AssignStmt graph_assignstmt) {
        this.graph_assignstmt = graph_assignstmt;
    }
    public graph_IfStmt getGraph_ifstmt() {
        return graph_ifstmt;
    }

    public void setGraph_ifstmt(graph_IfStmt graph_ifstmt) {
        this.graph_ifstmt = graph_ifstmt;
    }
    public graph_WhileStmt getGraph_whilestmt() {
        return graph_whilestmt;
    }

    public void setGraph_whilestmt(graph_WhileStmt graph_whilestmt) {
        this.graph_whilestmt = graph_whilestmt;
    }

}