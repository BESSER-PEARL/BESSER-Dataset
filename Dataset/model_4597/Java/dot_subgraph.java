





import java.util.List;
import java.util.ArrayList;

public class dot_subgraph extends stmt {

    private String name;





    private List<dot_stmt> dot_stmts;


    public dot_subgraph(
        String name    ) {
        super(
        );
        this.name = name;
        this.dot_stmts = new ArrayList<>();
    }

    public dot_subgraph(
        String name        ArrayList<dot_stmt> dot_stmts    ) {
        this.name = name;
        this.dot_stmts = dot_stmts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<dot_stmt> getDot_stmts() {
        return dot_stmts;
    }

    public void addDot_stmt(Dot_stmt dot_stmt) {
        this.dot_stmts.add(dot_stmt);
    }

}