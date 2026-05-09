





import java.util.List;
import java.util.ArrayList;

public class DOM_SimpleName extends Name {

    private String declaration;
    private String identifier;





    private DOM_VariableDeclaration dom_variabledeclaration;




    private DOM_MethodRef dom_methodref;




    private DOM_MethodRefParameter dom_methodrefparameter;




    private DOM_TypeParameter dom_typeparameter;




    private DOM_MemberValuePair dom_membervaluepair;




    private DOM_AbstractTypeDeclaration dom_abstracttypedeclaration;




    private DOM_MemberRef dom_memberref;


    public DOM_SimpleName(
        String declaration,        String identifier    ) {
        super(
        );
        this.declaration = declaration;
        this.identifier = identifier;
    }


    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public DOM_VariableDeclaration getDom_variabledeclaration() {
        return dom_variabledeclaration;
    }

    public void setDom_variabledeclaration(DOM_VariableDeclaration dom_variabledeclaration) {
        this.dom_variabledeclaration = dom_variabledeclaration;
    }
    public DOM_MethodRef getDom_methodref() {
        return dom_methodref;
    }

    public void setDom_methodref(DOM_MethodRef dom_methodref) {
        this.dom_methodref = dom_methodref;
    }
    public DOM_MethodRefParameter getDom_methodrefparameter() {
        return dom_methodrefparameter;
    }

    public void setDom_methodrefparameter(DOM_MethodRefParameter dom_methodrefparameter) {
        this.dom_methodrefparameter = dom_methodrefparameter;
    }
    public DOM_TypeParameter getDom_typeparameter() {
        return dom_typeparameter;
    }

    public void setDom_typeparameter(DOM_TypeParameter dom_typeparameter) {
        this.dom_typeparameter = dom_typeparameter;
    }
    public DOM_MemberValuePair getDom_membervaluepair() {
        return dom_membervaluepair;
    }

    public void setDom_membervaluepair(DOM_MemberValuePair dom_membervaluepair) {
        this.dom_membervaluepair = dom_membervaluepair;
    }
    public DOM_AbstractTypeDeclaration getDom_abstracttypedeclaration() {
        return dom_abstracttypedeclaration;
    }

    public void setDom_abstracttypedeclaration(DOM_AbstractTypeDeclaration dom_abstracttypedeclaration) {
        this.dom_abstracttypedeclaration = dom_abstracttypedeclaration;
    }
    public DOM_MemberRef getDom_memberref() {
        return dom_memberref;
    }

    public void setDom_memberref(DOM_MemberRef dom_memberref) {
        this.dom_memberref = dom_memberref;
    }

}