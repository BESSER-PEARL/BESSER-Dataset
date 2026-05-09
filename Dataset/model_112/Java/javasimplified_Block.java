





import java.util.List;
import java.util.ArrayList;

public class javasimplified_Block extends Statement {






    private List<javasimplified_Statement> javasimplified_statements;


    public javasimplified_Block(
    ) {
        super(
        );
        this.javasimplified_statements = new ArrayList<>();
    }

    public javasimplified_Block(
        ArrayList<javasimplified_Statement> javasimplified_statements    ) {
        this.javasimplified_statements = javasimplified_statements;
    }


    public List<javasimplified_Statement> getJavasimplified_statements() {
        return javasimplified_statements;
    }

    public void addJavasimplified_statement(Javasimplified_statement javasimplified_statement) {
        this.javasimplified_statements.add(javasimplified_statement);
    }

}