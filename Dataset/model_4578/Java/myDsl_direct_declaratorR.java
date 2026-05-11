





import java.util.List;
import java.util.ArrayList;

public class myDsl_direct_declaratorR  {






    private myDsl_assignment_expression mydsl_assignment_expression;




    private myDsl_IDENTIFIER mydsl_identifier;




    private List<myDsl_direct_declaratorR> mydsl_direct_declaratorrs;




    private myDsl_direct_declarator mydsl_direct_declarator;


    public myDsl_direct_declaratorR(
    ) {
        this.mydsl_direct_declaratorrs = new ArrayList<>();
    }

    public myDsl_direct_declaratorR(
        ArrayList<myDsl_direct_declaratorR> mydsl_direct_declaratorrs    ) {
        this.mydsl_direct_declaratorrs = mydsl_direct_declaratorrs;
    }


    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }
    public myDsl_IDENTIFIER getMydsl_identifier() {
        return mydsl_identifier;
    }

    public void setMydsl_identifier(myDsl_IDENTIFIER mydsl_identifier) {
        this.mydsl_identifier = mydsl_identifier;
    }
    public List<myDsl_direct_declaratorR> getMydsl_direct_declaratorrs() {
        return mydsl_direct_declaratorrs;
    }

    public void addMydsl_direct_declaratorr(Mydsl_direct_declaratorr mydsl_direct_declaratorr) {
        this.mydsl_direct_declaratorrs.add(mydsl_direct_declaratorr);
    }
    public myDsl_direct_declarator getMydsl_direct_declarator() {
        return mydsl_direct_declarator;
    }

    public void setMydsl_direct_declarator(myDsl_direct_declarator mydsl_direct_declarator) {
        this.mydsl_direct_declarator = mydsl_direct_declarator;
    }

}