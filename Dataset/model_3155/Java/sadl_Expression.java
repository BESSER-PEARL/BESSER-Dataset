





import java.util.List;
import java.util.ArrayList;

public class sadl_Expression  {

    private String func;





    private sadl_ExplicitValue sadl_explicitvalue;




    private sadl_Test sadl_test;




    private sadl_ElementSet sadl_elementset;




    private sadl_Expression sadl_expression;




    private sadl_Expr sadl_expr;




    private sadl_Query sadl_query;




    private List<sadl_Expression> sadl_expressions;




    private sadl_InstAttrSPV sadl_instattrspv;




    private sadl_ExistentialNegation sadl_existentialnegation;


    public sadl_Expression(
        String func    ) {
        this.func = func;
        this.sadl_expressions = new ArrayList<>();
    }

    public sadl_Expression(
        String func        ArrayList<sadl_Expression> sadl_expressions    ) {
        this.func = func;
        this.sadl_expressions = sadl_expressions;
    }

    public String getFunc() {
        return func;
    }

    public void setFunc(String func) {
        this.func = func;
    }

    public sadl_ExplicitValue getSadl_explicitvalue() {
        return sadl_explicitvalue;
    }

    public void setSadl_explicitvalue(sadl_ExplicitValue sadl_explicitvalue) {
        this.sadl_explicitvalue = sadl_explicitvalue;
    }
    public sadl_Test getSadl_test() {
        return sadl_test;
    }

    public void setSadl_test(sadl_Test sadl_test) {
        this.sadl_test = sadl_test;
    }
    public sadl_ElementSet getSadl_elementset() {
        return sadl_elementset;
    }

    public void setSadl_elementset(sadl_ElementSet sadl_elementset) {
        this.sadl_elementset = sadl_elementset;
    }
    public sadl_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sadl_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }
    public sadl_Expr getSadl_expr() {
        return sadl_expr;
    }

    public void setSadl_expr(sadl_Expr sadl_expr) {
        this.sadl_expr = sadl_expr;
    }
    public sadl_Query getSadl_query() {
        return sadl_query;
    }

    public void setSadl_query(sadl_Query sadl_query) {
        this.sadl_query = sadl_query;
    }
    public List<sadl_Expression> getSadl_expressions() {
        return sadl_expressions;
    }

    public void addSadl_expression(Sadl_expression sadl_expression) {
        this.sadl_expressions.add(sadl_expression);
    }
    public sadl_InstAttrSPV getSadl_instattrspv() {
        return sadl_instattrspv;
    }

    public void setSadl_instattrspv(sadl_InstAttrSPV sadl_instattrspv) {
        this.sadl_instattrspv = sadl_instattrspv;
    }
    public sadl_ExistentialNegation getSadl_existentialnegation() {
        return sadl_existentialnegation;
    }

    public void setSadl_existentialnegation(sadl_ExistentialNegation sadl_existentialnegation) {
        this.sadl_existentialnegation = sadl_existentialnegation;
    }

}