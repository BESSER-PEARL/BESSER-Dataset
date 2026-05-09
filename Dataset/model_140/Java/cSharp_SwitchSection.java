





import java.util.List;
import java.util.ArrayList;

public class cSharp_SwitchSection  {






    private List<cSharp_Statement> csharp_statements;




    private cSharp_SwitchStatement csharp_switchstatement;


    public cSharp_SwitchSection(
    ) {
        this.csharp_statements = new ArrayList<>();
    }

    public cSharp_SwitchSection(
        ArrayList<cSharp_Statement> csharp_statements    ) {
        this.csharp_statements = csharp_statements;
    }


    public List<cSharp_Statement> getCsharp_statements() {
        return csharp_statements;
    }

    public void addCsharp_statement(Csharp_statement csharp_statement) {
        this.csharp_statements.add(csharp_statement);
    }
    public cSharp_SwitchStatement getCsharp_switchstatement() {
        return csharp_switchstatement;
    }

    public void setCsharp_switchstatement(cSharp_SwitchStatement csharp_switchstatement) {
        this.csharp_switchstatement = csharp_switchstatement;
    }

}