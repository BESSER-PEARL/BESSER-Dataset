





import java.util.List;
import java.util.ArrayList;

public class minilang_Block  {






    private minilang_If minilang_if;




    private List<minilang_Statement> minilang_statements;




    private minilang_If minilang_if;


    public minilang_Block(
    ) {
        this.minilang_statements = new ArrayList<>();
    }

    public minilang_Block(
        ArrayList<minilang_Statement> minilang_statements    ) {
        this.minilang_statements = minilang_statements;
    }


    public minilang_If getMinilang_if() {
        return minilang_if;
    }

    public void setMinilang_if(minilang_If minilang_if) {
        this.minilang_if = minilang_if;
    }
    public List<minilang_Statement> getMinilang_statements() {
        return minilang_statements;
    }

    public void addMinilang_statement(Minilang_statement minilang_statement) {
        this.minilang_statements.add(minilang_statement);
    }
    public minilang_If getMinilang_if() {
        return minilang_if;
    }

    public void setMinilang_if(minilang_If minilang_if) {
        this.minilang_if = minilang_if;
    }

}