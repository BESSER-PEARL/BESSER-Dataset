





import java.util.List;
import java.util.ArrayList;

public class cSharp_PrimaryExpression2  {

    private String incrementeDecrement;





    private List<cSharp_Identifier> csharp_identifiers;




    private List<cSharp_ExpressionList> csharp_expressionlists;




    private List<cSharp_ArgumentList> csharp_argumentlists;




    private cSharp_PrimaryExpression csharp_primaryexpression;




    private List<cSharp_PrimaryExpression2> csharp_primaryexpression2s;


    public cSharp_PrimaryExpression2(
        String incrementeDecrement    ) {
        this.incrementeDecrement = incrementeDecrement;
        this.csharp_identifiers = new ArrayList<>();
        this.csharp_expressionlists = new ArrayList<>();
        this.csharp_argumentlists = new ArrayList<>();
        this.csharp_primaryexpression2s = new ArrayList<>();
    }

    public cSharp_PrimaryExpression2(
        String incrementeDecrement        ArrayList<cSharp_Identifier> csharp_identifiers,        ArrayList<cSharp_ExpressionList> csharp_expressionlists,        ArrayList<cSharp_ArgumentList> csharp_argumentlists,        ArrayList<cSharp_PrimaryExpression2> csharp_primaryexpression2s    ) {
        this.incrementeDecrement = incrementeDecrement;
        this.csharp_identifiers = csharp_identifiers;
        this.csharp_expressionlists = csharp_expressionlists;
        this.csharp_argumentlists = csharp_argumentlists;
        this.csharp_primaryexpression2s = csharp_primaryexpression2s;
    }

    public String getIncrementedecrement() {
        return incrementeDecrement;
    }

    public void setIncrementedecrement(String incrementeDecrement) {
        this.incrementeDecrement = incrementeDecrement;
    }

    public List<cSharp_Identifier> getCsharp_identifiers() {
        return csharp_identifiers;
    }

    public void addCsharp_identifier(Csharp_identifier csharp_identifier) {
        this.csharp_identifiers.add(csharp_identifier);
    }
    public List<cSharp_ExpressionList> getCsharp_expressionlists() {
        return csharp_expressionlists;
    }

    public void addCsharp_expressionlist(Csharp_expressionlist csharp_expressionlist) {
        this.csharp_expressionlists.add(csharp_expressionlist);
    }
    public List<cSharp_ArgumentList> getCsharp_argumentlists() {
        return csharp_argumentlists;
    }

    public void addCsharp_argumentlist(Csharp_argumentlist csharp_argumentlist) {
        this.csharp_argumentlists.add(csharp_argumentlist);
    }
    public cSharp_PrimaryExpression getCsharp_primaryexpression() {
        return csharp_primaryexpression;
    }

    public void setCsharp_primaryexpression(cSharp_PrimaryExpression csharp_primaryexpression) {
        this.csharp_primaryexpression = csharp_primaryexpression;
    }
    public List<cSharp_PrimaryExpression2> getCsharp_primaryexpression2s() {
        return csharp_primaryexpression2s;
    }

    public void addCsharp_primaryexpression2(Csharp_primaryexpression2 csharp_primaryexpression2) {
        this.csharp_primaryexpression2s.add(csharp_primaryexpression2);
    }

}