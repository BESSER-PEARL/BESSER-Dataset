





import java.util.List;
import java.util.ArrayList;

public class aS3_assignmentExpression extends nonemptyElementList, encapsulatedExpression, element, parameterDefault, Expression {






    private aS3_VariableDeclaration as3_variabledeclaration;




    private List<aS3_EObject> as3_eobjects;




    private aS3_MemberVariableDeclaration as3_membervariabledeclaration;


    public aS3_assignmentExpression(
    ) {
        super(
        );
        this.as3_eobjects = new ArrayList<>();
    }

    public aS3_assignmentExpression(
        ArrayList<aS3_EObject> as3_eobjects    ) {
        this.as3_eobjects = as3_eobjects;
    }


    public aS3_VariableDeclaration getAs3_variabledeclaration() {
        return as3_variabledeclaration;
    }

    public void setAs3_variabledeclaration(aS3_VariableDeclaration as3_variabledeclaration) {
        this.as3_variabledeclaration = as3_variabledeclaration;
    }
    public List<aS3_EObject> getAs3_eobjects() {
        return as3_eobjects;
    }

    public void addAs3_eobject(As3_eobject as3_eobject) {
        this.as3_eobjects.add(as3_eobject);
    }
    public aS3_MemberVariableDeclaration getAs3_membervariabledeclaration() {
        return as3_membervariabledeclaration;
    }

    public void setAs3_membervariabledeclaration(aS3_MemberVariableDeclaration as3_membervariabledeclaration) {
        this.as3_membervariabledeclaration = as3_membervariabledeclaration;
    }

}