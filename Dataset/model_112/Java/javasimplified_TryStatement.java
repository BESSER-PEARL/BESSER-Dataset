





import java.util.List;
import java.util.ArrayList;

public class javasimplified_TryStatement extends Statement {






    private List<javasimplified_CatchStatment> javasimplified_catchstatments;




    private javasimplified_Statement javasimplified_statement;


    public javasimplified_TryStatement(
    ) {
        super(
        );
        this.javasimplified_catchstatments = new ArrayList<>();
    }

    public javasimplified_TryStatement(
        ArrayList<javasimplified_CatchStatment> javasimplified_catchstatments    ) {
        this.javasimplified_catchstatments = javasimplified_catchstatments;
    }


    public List<javasimplified_CatchStatment> getJavasimplified_catchstatments() {
        return javasimplified_catchstatments;
    }

    public void addJavasimplified_catchstatment(Javasimplified_catchstatment javasimplified_catchstatment) {
        this.javasimplified_catchstatments.add(javasimplified_catchstatment);
    }
    public javasimplified_Statement getJavasimplified_statement() {
        return javasimplified_statement;
    }

    public void setJavasimplified_statement(javasimplified_Statement javasimplified_statement) {
        this.javasimplified_statement = javasimplified_statement;
    }

}