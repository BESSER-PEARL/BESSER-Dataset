





import java.util.List;
import java.util.ArrayList;

public class leek_Script  {






    private List<leek_Statement> leek_statements;


    public leek_Script(
    ) {
        this.leek_statements = new ArrayList<>();
    }

    public leek_Script(
        ArrayList<leek_Statement> leek_statements    ) {
        this.leek_statements = leek_statements;
    }


    public List<leek_Statement> getLeek_statements() {
        return leek_statements;
    }

    public void addLeek_statement(Leek_statement leek_statement) {
        this.leek_statements.add(leek_statement);
    }

}