





import java.util.List;
import java.util.ArrayList;

public class c_sharp_expressions_UnaryExpression  {






    private List<PrimaryExtendedExpressionType> primaryextendedexpressiontypes;




    private PrimaryExpression primaryexpression;


    public c_sharp_expressions_UnaryExpression(
    ) {
        this.primaryextendedexpressiontypes = new ArrayList<>();
    }

    public c_sharp_expressions_UnaryExpression(
        ArrayList<PrimaryExtendedExpressionType> primaryextendedexpressiontypes    ) {
        this.primaryextendedexpressiontypes = primaryextendedexpressiontypes;
    }


    public List<PrimaryExtendedExpressionType> getPrimaryextendedexpressiontypes() {
        return primaryextendedexpressiontypes;
    }

    public void addPrimaryextendedexpressiontype(Primaryextendedexpressiontype primaryextendedexpressiontype) {
        this.primaryextendedexpressiontypes.add(primaryextendedexpressiontype);
    }
    public PrimaryExpression getPrimaryexpression() {
        return primaryexpression;
    }

    public void setPrimaryexpression(PrimaryExpression primaryexpression) {
        this.primaryexpression = primaryexpression;
    }

}