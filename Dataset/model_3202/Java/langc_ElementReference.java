





import java.util.List;
import java.util.ArrayList;

public class langc_ElementReference extends BindableValue {

    private String cvQualifier;
    private String pointerSpec;





    private langc_Typedef langc_typedef;




    private langc_VariableDeclaration langc_variabledeclaration;




    private langc_CastExpr langc_castexpr;




    private langc_FunctionPointer langc_functionpointer;




    private langc_FunctionPointer langc_functionpointer;


    public langc_ElementReference(
        String cvQualifier,        String pointerSpec    ) {
        super(
        );
        this.cvQualifier = cvQualifier;
        this.pointerSpec = pointerSpec;
    }


    public String getCvqualifier() {
        return cvQualifier;
    }

    public void setCvqualifier(String cvQualifier) {
        this.cvQualifier = cvQualifier;
    }
    public String getPointerspec() {
        return pointerSpec;
    }

    public void setPointerspec(String pointerSpec) {
        this.pointerSpec = pointerSpec;
    }

    public langc_Typedef getLangc_typedef() {
        return langc_typedef;
    }

    public void setLangc_typedef(langc_Typedef langc_typedef) {
        this.langc_typedef = langc_typedef;
    }
    public langc_VariableDeclaration getLangc_variabledeclaration() {
        return langc_variabledeclaration;
    }

    public void setLangc_variabledeclaration(langc_VariableDeclaration langc_variabledeclaration) {
        this.langc_variabledeclaration = langc_variabledeclaration;
    }
    public langc_CastExpr getLangc_castexpr() {
        return langc_castexpr;
    }

    public void setLangc_castexpr(langc_CastExpr langc_castexpr) {
        this.langc_castexpr = langc_castexpr;
    }
    public langc_FunctionPointer getLangc_functionpointer() {
        return langc_functionpointer;
    }

    public void setLangc_functionpointer(langc_FunctionPointer langc_functionpointer) {
        this.langc_functionpointer = langc_functionpointer;
    }
    public langc_FunctionPointer getLangc_functionpointer() {
        return langc_functionpointer;
    }

    public void setLangc_functionpointer(langc_FunctionPointer langc_functionpointer) {
        this.langc_functionpointer = langc_functionpointer;
    }

}