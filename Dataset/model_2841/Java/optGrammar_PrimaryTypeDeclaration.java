





import java.util.List;
import java.util.ArrayList;

public class optGrammar_PrimaryTypeDeclaration extends PrimaryTypeDefinitionDeclaration {

    private boolean constant;
    private String name;





    private optGrammar_VisibilityLiteral optgrammar_visibilityliteral;




    private optGrammar_PrimaryTypeDefinitionDeclaration optgrammar_primarytypedefinitiondeclaration;


    public optGrammar_PrimaryTypeDeclaration(
        boolean constant,        String name    ) {
        super(
        );
        this.constant = constant;
        this.name = name;
    }


    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public optGrammar_VisibilityLiteral getOptgrammar_visibilityliteral() {
        return optgrammar_visibilityliteral;
    }

    public void setOptgrammar_visibilityliteral(optGrammar_VisibilityLiteral optgrammar_visibilityliteral) {
        this.optgrammar_visibilityliteral = optgrammar_visibilityliteral;
    }
    public optGrammar_PrimaryTypeDefinitionDeclaration getOptgrammar_primarytypedefinitiondeclaration() {
        return optgrammar_primarytypedefinitiondeclaration;
    }

    public void setOptgrammar_primarytypedefinitiondeclaration(optGrammar_PrimaryTypeDefinitionDeclaration optgrammar_primarytypedefinitiondeclaration) {
        this.optgrammar_primarytypedefinitiondeclaration = optgrammar_primarytypedefinitiondeclaration;
    }

}