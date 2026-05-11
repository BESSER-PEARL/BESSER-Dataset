





import java.util.List;
import java.util.ArrayList;

public class dbl_LocalScope  {






    private dbl_Class dbl_class;




    private List<dbl_Statement> dbl_statements;


    public dbl_LocalScope(
    ) {
        this.dbl_statements = new ArrayList<>();
    }

    public dbl_LocalScope(
        ArrayList<dbl_Statement> dbl_statements    ) {
        this.dbl_statements = dbl_statements;
    }


    public dbl_Class getDbl_class() {
        return dbl_class;
    }

    public void setDbl_class(dbl_Class dbl_class) {
        this.dbl_class = dbl_class;
    }
    public List<dbl_Statement> getDbl_statements() {
        return dbl_statements;
    }

    public void addDbl_statement(Dbl_statement dbl_statement) {
        this.dbl_statements.add(dbl_statement);
    }

}