





import java.util.List;
import java.util.ArrayList;

public class myDsl_direct_declarator2  {

    private String static;





    private myDsl_assignment_expression mydsl_assignment_expression;




    private List<myDsl_direct_declarator2> mydsl_direct_declarator2s;


    public myDsl_direct_declarator2(
        String static    ) {
        this.static = static;
        this.mydsl_direct_declarator2s = new ArrayList<>();
    }

    public myDsl_direct_declarator2(
        String static        ArrayList<myDsl_direct_declarator2> mydsl_direct_declarator2s    ) {
        this.static = static;
        this.mydsl_direct_declarator2s = mydsl_direct_declarator2s;
    }

    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }

    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }
    public List<myDsl_direct_declarator2> getMydsl_direct_declarator2s() {
        return mydsl_direct_declarator2s;
    }

    public void addMydsl_direct_declarator2(Mydsl_direct_declarator2 mydsl_direct_declarator2) {
        this.mydsl_direct_declarator2s.add(mydsl_direct_declarator2);
    }

}