





import java.util.List;
import java.util.ArrayList;

public class javaDsl_Primary  {

    private String fields;





    private javaDsl_PostfixExpression javadsl_postfixexpression;




    private javaDsl_MethodInvocation javadsl_methodinvocation;




    private List<javaDsl_ArgumentList> javadsl_argumentlists;


    public javaDsl_Primary(
        String fields    ) {
        this.fields = fields;
        this.javadsl_argumentlists = new ArrayList<>();
    }

    public javaDsl_Primary(
        String fields        ArrayList<javaDsl_ArgumentList> javadsl_argumentlists    ) {
        this.fields = fields;
        this.javadsl_argumentlists = javadsl_argumentlists;
    }

    public String getFields() {
        return fields;
    }

    public void setFields(String fields) {
        this.fields = fields;
    }

    public javaDsl_PostfixExpression getJavadsl_postfixexpression() {
        return javadsl_postfixexpression;
    }

    public void setJavadsl_postfixexpression(javaDsl_PostfixExpression javadsl_postfixexpression) {
        this.javadsl_postfixexpression = javadsl_postfixexpression;
    }
    public javaDsl_MethodInvocation getJavadsl_methodinvocation() {
        return javadsl_methodinvocation;
    }

    public void setJavadsl_methodinvocation(javaDsl_MethodInvocation javadsl_methodinvocation) {
        this.javadsl_methodinvocation = javadsl_methodinvocation;
    }
    public List<javaDsl_ArgumentList> getJavadsl_argumentlists() {
        return javadsl_argumentlists;
    }

    public void addJavadsl_argumentlist(Javadsl_argumentlist javadsl_argumentlist) {
        this.javadsl_argumentlists.add(javadsl_argumentlist);
    }

}