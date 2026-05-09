





import java.util.List;
import java.util.ArrayList;

public class c_sharp_expressions_UnaryExpression  {






    private PreDecrementExpression predecrementexpression;




    private CastExpression castexpression;




    private PrimaryExpression primaryexpression;




    private List<PrimaryExtendedExpressionType> primaryextendedexpressiontypes;




    private PreIncrementExpression preincrementexpression;


    public c_sharp_expressions_UnaryExpression(
    ) {
        this.primaryextendedexpressiontypes = new ArrayList<>();
    }

    public c_sharp_expressions_UnaryExpression(
        ArrayList<PrimaryExtendedExpressionType> primaryextendedexpressiontypes    ) {
        this.primaryextendedexpressiontypes = primaryextendedexpressiontypes;
    }


    public PreDecrementExpression getPredecrementexpression() {
        return predecrementexpression;
    }

    public void setPredecrementexpression(PreDecrementExpression predecrementexpression) {
        this.predecrementexpression = predecrementexpression;
    }
    public CastExpression getCastexpression() {
        return castexpression;
    }

    public void setCastexpression(CastExpression castexpression) {
        this.castexpression = castexpression;
    }
    public PrimaryExpression getPrimaryexpression() {
        return primaryexpression;
    }

    public void setPrimaryexpression(PrimaryExpression primaryexpression) {
        this.primaryexpression = primaryexpression;
    }
    public List<PrimaryExtendedExpressionType> getPrimaryextendedexpressiontypes() {
        return primaryextendedexpressiontypes;
    }

    public void addPrimaryextendedexpressiontype(Primaryextendedexpressiontype primaryextendedexpressiontype) {
        this.primaryextendedexpressiontypes.add(primaryextendedexpressiontype);
    }
    public PreIncrementExpression getPreincrementexpression() {
        return preincrementexpression;
    }

    public void setPreincrementexpression(PreIncrementExpression preincrementexpression) {
        this.preincrementexpression = preincrementexpression;
    }

}