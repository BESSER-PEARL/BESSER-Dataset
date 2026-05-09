





import java.util.List;
import java.util.ArrayList;

public class cSharp_ForStatement  {






    private cSharp_IterationStatement csharp_iterationstatement;




    private List<cSharp_Expression> csharp_expressions;




    private cSharp_EmbeddedStatement csharp_embeddedstatement;


    public cSharp_ForStatement(
    ) {
        this.csharp_expressions = new ArrayList<>();
    }

    public cSharp_ForStatement(
        ArrayList<cSharp_Expression> csharp_expressions    ) {
        this.csharp_expressions = csharp_expressions;
    }


    public cSharp_IterationStatement getCsharp_iterationstatement() {
        return csharp_iterationstatement;
    }

    public void setCsharp_iterationstatement(cSharp_IterationStatement csharp_iterationstatement) {
        this.csharp_iterationstatement = csharp_iterationstatement;
    }
    public List<cSharp_Expression> getCsharp_expressions() {
        return csharp_expressions;
    }

    public void addCsharp_expression(Csharp_expression csharp_expression) {
        this.csharp_expressions.add(csharp_expression);
    }
    public cSharp_EmbeddedStatement getCsharp_embeddedstatement() {
        return csharp_embeddedstatement;
    }

    public void setCsharp_embeddedstatement(cSharp_EmbeddedStatement csharp_embeddedstatement) {
        this.csharp_embeddedstatement = csharp_embeddedstatement;
    }

}