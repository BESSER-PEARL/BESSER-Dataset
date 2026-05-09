





import java.util.List;
import java.util.ArrayList;

public class cSharp_PrimaryExpression  {

    private String rankSpecifier;
    private String literal;
    private String predefinedType;





    private cSharp_ArrayType csharp_arraytype;




    private cSharp_Expression csharp_expression;




    private cSharp_ArrayInitializer csharp_arrayinitializer;




    private cSharp_UnaryExpression csharp_unaryexpression;




    private cSharp_ExpressionList csharp_expressionlist;




    private List<cSharp_ArrayInitializer> csharp_arrayinitializers;




    private cSharp_Identifier csharp_identifier;


    public cSharp_PrimaryExpression(
        String rankSpecifier,        String literal,        String predefinedType    ) {
        this.rankSpecifier = rankSpecifier;
        this.literal = literal;
        this.predefinedType = predefinedType;
        this.csharp_arrayinitializers = new ArrayList<>();
    }

    public cSharp_PrimaryExpression(
        String rankSpecifier,        String literal,        String predefinedType        ArrayList<cSharp_ArrayInitializer> csharp_arrayinitializers    ) {
        this.rankSpecifier = rankSpecifier;
        this.literal = literal;
        this.predefinedType = predefinedType;
        this.csharp_arrayinitializers = csharp_arrayinitializers;
    }

    public String getRankspecifier() {
        return rankSpecifier;
    }

    public void setRankspecifier(String rankSpecifier) {
        this.rankSpecifier = rankSpecifier;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public String getPredefinedtype() {
        return predefinedType;
    }

    public void setPredefinedtype(String predefinedType) {
        this.predefinedType = predefinedType;
    }

    public cSharp_ArrayType getCsharp_arraytype() {
        return csharp_arraytype;
    }

    public void setCsharp_arraytype(cSharp_ArrayType csharp_arraytype) {
        this.csharp_arraytype = csharp_arraytype;
    }
    public cSharp_Expression getCsharp_expression() {
        return csharp_expression;
    }

    public void setCsharp_expression(cSharp_Expression csharp_expression) {
        this.csharp_expression = csharp_expression;
    }
    public cSharp_ArrayInitializer getCsharp_arrayinitializer() {
        return csharp_arrayinitializer;
    }

    public void setCsharp_arrayinitializer(cSharp_ArrayInitializer csharp_arrayinitializer) {
        this.csharp_arrayinitializer = csharp_arrayinitializer;
    }
    public cSharp_UnaryExpression getCsharp_unaryexpression() {
        return csharp_unaryexpression;
    }

    public void setCsharp_unaryexpression(cSharp_UnaryExpression csharp_unaryexpression) {
        this.csharp_unaryexpression = csharp_unaryexpression;
    }
    public cSharp_ExpressionList getCsharp_expressionlist() {
        return csharp_expressionlist;
    }

    public void setCsharp_expressionlist(cSharp_ExpressionList csharp_expressionlist) {
        this.csharp_expressionlist = csharp_expressionlist;
    }
    public List<cSharp_ArrayInitializer> getCsharp_arrayinitializers() {
        return csharp_arrayinitializers;
    }

    public void addCsharp_arrayinitializer(Csharp_arrayinitializer csharp_arrayinitializer) {
        this.csharp_arrayinitializers.add(csharp_arrayinitializer);
    }
    public cSharp_Identifier getCsharp_identifier() {
        return csharp_identifier;
    }

    public void setCsharp_identifier(cSharp_Identifier csharp_identifier) {
        this.csharp_identifier = csharp_identifier;
    }

}