





import java.util.List;
import java.util.ArrayList;

public class asmeta_definitions_Function extends Classifier {

    private String arity;





    private FunctionDefinition functiondefinition;




    private domains_Domain domains_domain;




    private domains_Domain domains_domain;




    private Signature signature;


    public asmeta_definitions_Function(
        String arity    ) {
        super(
        );
        this.arity = arity;
    }


    public String getArity() {
        return arity;
    }

    public void setArity(String arity) {
        this.arity = arity;
    }

    public FunctionDefinition getFunctiondefinition() {
        return functiondefinition;
    }

    public void setFunctiondefinition(FunctionDefinition functiondefinition) {
        this.functiondefinition = functiondefinition;
    }
    public domains_Domain getDomains_domain() {
        return domains_domain;
    }

    public void setDomains_domain(domains_Domain domains_domain) {
        this.domains_domain = domains_domain;
    }
    public domains_Domain getDomains_domain() {
        return domains_domain;
    }

    public void setDomains_domain(domains_Domain domains_domain) {
        this.domains_domain = domains_domain;
    }
    public Signature getSignature() {
        return signature;
    }

    public void setSignature(Signature signature) {
        this.signature = signature;
    }

}