





import java.util.List;
import java.util.ArrayList;

public class JDTAST_Expression extends ASTNode {

    private String resolveBoxing;
    private String resolveUnboxing;





    private JDTAST_IType jdtast_itype;




    private JDTAST_MemberValuePair jdtast_membervaluepair;




    private JDTAST_VariableDeclaration jdtast_variabledeclaration;


    public JDTAST_Expression(
        String resolveBoxing,        String resolveUnboxing    ) {
        super(
        );
        this.resolveBoxing = resolveBoxing;
        this.resolveUnboxing = resolveUnboxing;
    }


    public String getResolveboxing() {
        return resolveBoxing;
    }

    public void setResolveboxing(String resolveBoxing) {
        this.resolveBoxing = resolveBoxing;
    }
    public String getResolveunboxing() {
        return resolveUnboxing;
    }

    public void setResolveunboxing(String resolveUnboxing) {
        this.resolveUnboxing = resolveUnboxing;
    }

    public JDTAST_IType getJdtast_itype() {
        return jdtast_itype;
    }

    public void setJdtast_itype(JDTAST_IType jdtast_itype) {
        this.jdtast_itype = jdtast_itype;
    }
    public JDTAST_MemberValuePair getJdtast_membervaluepair() {
        return jdtast_membervaluepair;
    }

    public void setJdtast_membervaluepair(JDTAST_MemberValuePair jdtast_membervaluepair) {
        this.jdtast_membervaluepair = jdtast_membervaluepair;
    }
    public JDTAST_VariableDeclaration getJdtast_variabledeclaration() {
        return jdtast_variabledeclaration;
    }

    public void setJdtast_variabledeclaration(JDTAST_VariableDeclaration jdtast_variabledeclaration) {
        this.jdtast_variabledeclaration = jdtast_variabledeclaration;
    }

}