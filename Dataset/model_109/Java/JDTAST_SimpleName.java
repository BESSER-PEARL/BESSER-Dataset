





import java.util.List;
import java.util.ArrayList;

public class JDTAST_SimpleName extends Name {

    private String declaration;
    private String identifier;





    private JDTAST_VariableDeclaration jdtast_variabledeclaration;




    private JDTAST_MemberValuePair jdtast_membervaluepair;




    private JDTAST_AbstractTypeDeclaration jdtast_abstracttypedeclaration;




    private JDTAST_TypeParameter jdtast_typeparameter;




    private JDTAST_MethodRef jdtast_methodref;




    private JDTAST_MemberRef jdtast_memberref;




    private JDTAST_MethodRefParameter jdtast_methodrefparameter;


    public JDTAST_SimpleName(
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

    public JDTAST_VariableDeclaration getJdtast_variabledeclaration() {
        return jdtast_variabledeclaration;
    }

    public void setJdtast_variabledeclaration(JDTAST_VariableDeclaration jdtast_variabledeclaration) {
        this.jdtast_variabledeclaration = jdtast_variabledeclaration;
    }
    public JDTAST_MemberValuePair getJdtast_membervaluepair() {
        return jdtast_membervaluepair;
    }

    public void setJdtast_membervaluepair(JDTAST_MemberValuePair jdtast_membervaluepair) {
        this.jdtast_membervaluepair = jdtast_membervaluepair;
    }
    public JDTAST_AbstractTypeDeclaration getJdtast_abstracttypedeclaration() {
        return jdtast_abstracttypedeclaration;
    }

    public void setJdtast_abstracttypedeclaration(JDTAST_AbstractTypeDeclaration jdtast_abstracttypedeclaration) {
        this.jdtast_abstracttypedeclaration = jdtast_abstracttypedeclaration;
    }
    public JDTAST_TypeParameter getJdtast_typeparameter() {
        return jdtast_typeparameter;
    }

    public void setJdtast_typeparameter(JDTAST_TypeParameter jdtast_typeparameter) {
        this.jdtast_typeparameter = jdtast_typeparameter;
    }
    public JDTAST_MethodRef getJdtast_methodref() {
        return jdtast_methodref;
    }

    public void setJdtast_methodref(JDTAST_MethodRef jdtast_methodref) {
        this.jdtast_methodref = jdtast_methodref;
    }
    public JDTAST_MemberRef getJdtast_memberref() {
        return jdtast_memberref;
    }

    public void setJdtast_memberref(JDTAST_MemberRef jdtast_memberref) {
        this.jdtast_memberref = jdtast_memberref;
    }
    public JDTAST_MethodRefParameter getJdtast_methodrefparameter() {
        return jdtast_methodrefparameter;
    }

    public void setJdtast_methodrefparameter(JDTAST_MethodRefParameter jdtast_methodrefparameter) {
        this.jdtast_methodrefparameter = jdtast_methodrefparameter;
    }

}