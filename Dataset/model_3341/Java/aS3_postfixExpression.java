





import java.util.List;
import java.util.ArrayList;

public class aS3_postfixExpression extends unaryExpressionNotPlusMinus {






    private List<aS3_propOrIdent> as3_proporidents;




    private List<aS3_Expression> as3_expressions;




    private List<aS3_qualifiedIdentifier> as3_qualifiedidentifiers;




    private List<aS3_e4xAttributeIdentifier> as3_e4xattributeidentifiers;


    public aS3_postfixExpression(
    ) {
        super(
        );
        this.as3_proporidents = new ArrayList<>();
        this.as3_expressions = new ArrayList<>();
        this.as3_qualifiedidentifiers = new ArrayList<>();
        this.as3_e4xattributeidentifiers = new ArrayList<>();
    }

    public aS3_postfixExpression(
        ArrayList<aS3_propOrIdent> as3_proporidents,        ArrayList<aS3_Expression> as3_expressions,        ArrayList<aS3_qualifiedIdentifier> as3_qualifiedidentifiers,        ArrayList<aS3_e4xAttributeIdentifier> as3_e4xattributeidentifiers    ) {
        this.as3_proporidents = as3_proporidents;
        this.as3_expressions = as3_expressions;
        this.as3_qualifiedidentifiers = as3_qualifiedidentifiers;
        this.as3_e4xattributeidentifiers = as3_e4xattributeidentifiers;
    }


    public List<aS3_propOrIdent> getAs3_proporidents() {
        return as3_proporidents;
    }

    public void addAs3_proporident(As3_proporident as3_proporident) {
        this.as3_proporidents.add(as3_proporident);
    }
    public List<aS3_Expression> getAs3_expressions() {
        return as3_expressions;
    }

    public void addAs3_expression(As3_expression as3_expression) {
        this.as3_expressions.add(as3_expression);
    }
    public List<aS3_qualifiedIdentifier> getAs3_qualifiedidentifiers() {
        return as3_qualifiedidentifiers;
    }

    public void addAs3_qualifiedidentifier(As3_qualifiedidentifier as3_qualifiedidentifier) {
        this.as3_qualifiedidentifiers.add(as3_qualifiedidentifier);
    }
    public List<aS3_e4xAttributeIdentifier> getAs3_e4xattributeidentifiers() {
        return as3_e4xattributeidentifiers;
    }

    public void addAs3_e4xattributeidentifier(As3_e4xattributeidentifier as3_e4xattributeidentifier) {
        this.as3_e4xattributeidentifiers.add(as3_e4xattributeidentifier);
    }

}