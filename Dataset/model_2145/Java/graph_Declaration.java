





import java.util.List;
import java.util.ArrayList;

public class graph_Declaration  {

    private String type;
    private String name;





    private graph_AssignStmt graph_assignstmt;




    private graph_MoveStmt graph_movestmt;




    private graph_Program graph_program;


    public graph_Declaration(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public graph_AssignStmt getGraph_assignstmt() {
        return graph_assignstmt;
    }

    public void setGraph_assignstmt(graph_AssignStmt graph_assignstmt) {
        this.graph_assignstmt = graph_assignstmt;
    }
    public graph_MoveStmt getGraph_movestmt() {
        return graph_movestmt;
    }

    public void setGraph_movestmt(graph_MoveStmt graph_movestmt) {
        this.graph_movestmt = graph_movestmt;
    }
    public graph_Program getGraph_program() {
        return graph_program;
    }

    public void setGraph_program(graph_Program graph_program) {
        this.graph_program = graph_program;
    }

}