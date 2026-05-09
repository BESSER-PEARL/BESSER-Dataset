





import java.util.List;
import java.util.ArrayList;

public class gastm_QualifiedIdentifierReference extends NameReference {






    private gastm_Expression gastm_expression;




    private gastm_IdentifierReference gastm_identifierreference;


    public gastm_QualifiedIdentifierReference(
    ) {
        super(
        );
    }



    public gastm_Expression getGastm_expression() {
        return gastm_expression;
    }

    public void setGastm_expression(gastm_Expression gastm_expression) {
        this.gastm_expression = gastm_expression;
    }
    public gastm_IdentifierReference getGastm_identifierreference() {
        return gastm_identifierreference;
    }

    public void setGastm_identifierreference(gastm_IdentifierReference gastm_identifierreference) {
        this.gastm_identifierreference = gastm_identifierreference;
    }

}