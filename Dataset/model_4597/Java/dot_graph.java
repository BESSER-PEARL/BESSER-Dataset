





import java.util.List;
import java.util.ArrayList;

public class dot_graph  {

    private String name;
    private String type;
    private boolean strict;





    private List<dot_stmt> dot_stmts;




    private dot_graphvizmodel dot_graphvizmodel;


    public dot_graph(
        String name,        String type,        boolean strict    ) {
        this.name = name;
        this.type = type;
        this.strict = strict;
        this.dot_stmts = new ArrayList<>();
    }

    public dot_graph(
        String name,        String type,        boolean strict        ArrayList<dot_stmt> dot_stmts    ) {
        this.name = name;
        this.type = type;
        this.strict = strict;
        this.dot_stmts = dot_stmts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }

    public List<dot_stmt> getDot_stmts() {
        return dot_stmts;
    }

    public void addDot_stmt(Dot_stmt dot_stmt) {
        this.dot_stmts.add(dot_stmt);
    }
    public dot_graphvizmodel getDot_graphvizmodel() {
        return dot_graphvizmodel;
    }

    public void setDot_graphvizmodel(dot_graphvizmodel dot_graphvizmodel) {
        this.dot_graphvizmodel = dot_graphvizmodel;
    }

}