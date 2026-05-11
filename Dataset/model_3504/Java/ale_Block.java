





import java.util.List;
import java.util.ArrayList;

public class ale_Block  {






    private ale_If ale_if;




    private ale_While ale_while;




    private List<ale_Statement> ale_statements;




    private ale_Operation ale_operation;




    private ale_If ale_if;




    private ale_ForEach ale_foreach;


    public ale_Block(
    ) {
        this.ale_statements = new ArrayList<>();
    }

    public ale_Block(
        ArrayList<ale_Statement> ale_statements    ) {
        this.ale_statements = ale_statements;
    }


    public ale_If getAle_if() {
        return ale_if;
    }

    public void setAle_if(ale_If ale_if) {
        this.ale_if = ale_if;
    }
    public ale_While getAle_while() {
        return ale_while;
    }

    public void setAle_while(ale_While ale_while) {
        this.ale_while = ale_while;
    }
    public List<ale_Statement> getAle_statements() {
        return ale_statements;
    }

    public void addAle_statement(Ale_statement ale_statement) {
        this.ale_statements.add(ale_statement);
    }
    public ale_Operation getAle_operation() {
        return ale_operation;
    }

    public void setAle_operation(ale_Operation ale_operation) {
        this.ale_operation = ale_operation;
    }
    public ale_If getAle_if() {
        return ale_if;
    }

    public void setAle_if(ale_If ale_if) {
        this.ale_if = ale_if;
    }
    public ale_ForEach getAle_foreach() {
        return ale_foreach;
    }

    public void setAle_foreach(ale_ForEach ale_foreach) {
        this.ale_foreach = ale_foreach;
    }

}