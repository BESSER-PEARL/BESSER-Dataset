





import java.util.List;
import java.util.ArrayList;

public class eol_CollectionExpression extends LiteralExpression {






    private List<eol_LiteralExpression> eol_literalexpressions;




    private eol_Type eol_type;




    private eol_CollectionInitValue eol_collectioninitvalue;


    public eol_CollectionExpression(
    ) {
        super(
        );
        this.eol_literalexpressions = new ArrayList<>();
    }

    public eol_CollectionExpression(
        ArrayList<eol_LiteralExpression> eol_literalexpressions    ) {
        this.eol_literalexpressions = eol_literalexpressions;
    }


    public List<eol_LiteralExpression> getEol_literalexpressions() {
        return eol_literalexpressions;
    }

    public void addEol_literalexpression(Eol_literalexpression eol_literalexpression) {
        this.eol_literalexpressions.add(eol_literalexpression);
    }
    public eol_Type getEol_type() {
        return eol_type;
    }

    public void setEol_type(eol_Type eol_type) {
        this.eol_type = eol_type;
    }
    public eol_CollectionInitValue getEol_collectioninitvalue() {
        return eol_collectioninitvalue;
    }

    public void setEol_collectioninitvalue(eol_CollectionInitValue eol_collectioninitvalue) {
        this.eol_collectioninitvalue = eol_collectioninitvalue;
    }

}