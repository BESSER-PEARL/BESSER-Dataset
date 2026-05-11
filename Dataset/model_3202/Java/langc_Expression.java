





import java.util.List;
import java.util.ArrayList;

public class langc_Expression  {

    private int precendence;





    private langc_SwitchStatement langc_switchstatement;




    private langc_MemberAccess langc_memberaccess;




    private langc_CastExpr langc_castexpr;




    private langc_VariableDeclaration langc_variabledeclaration;




    private langc_BinaryOperation langc_binaryoperation;




    private langc_ExpressionStatement langc_expressionstatement;




    private langc_ElementReference langc_elementreference;




    private langc_Macro langc_macro;




    private langc_ElementReference langc_elementreference;




    private langc_BinaryOperation langc_binaryoperation;


    public langc_Expression(
        int precendence    ) {
        this.precendence = precendence;
    }


    public int getPrecendence() {
        return precendence;
    }

    public void setPrecendence(int precendence) {
        this.precendence = precendence;
    }

    public langc_SwitchStatement getLangc_switchstatement() {
        return langc_switchstatement;
    }

    public void setLangc_switchstatement(langc_SwitchStatement langc_switchstatement) {
        this.langc_switchstatement = langc_switchstatement;
    }
    public langc_MemberAccess getLangc_memberaccess() {
        return langc_memberaccess;
    }

    public void setLangc_memberaccess(langc_MemberAccess langc_memberaccess) {
        this.langc_memberaccess = langc_memberaccess;
    }
    public langc_CastExpr getLangc_castexpr() {
        return langc_castexpr;
    }

    public void setLangc_castexpr(langc_CastExpr langc_castexpr) {
        this.langc_castexpr = langc_castexpr;
    }
    public langc_VariableDeclaration getLangc_variabledeclaration() {
        return langc_variabledeclaration;
    }

    public void setLangc_variabledeclaration(langc_VariableDeclaration langc_variabledeclaration) {
        this.langc_variabledeclaration = langc_variabledeclaration;
    }
    public langc_BinaryOperation getLangc_binaryoperation() {
        return langc_binaryoperation;
    }

    public void setLangc_binaryoperation(langc_BinaryOperation langc_binaryoperation) {
        this.langc_binaryoperation = langc_binaryoperation;
    }
    public langc_ExpressionStatement getLangc_expressionstatement() {
        return langc_expressionstatement;
    }

    public void setLangc_expressionstatement(langc_ExpressionStatement langc_expressionstatement) {
        this.langc_expressionstatement = langc_expressionstatement;
    }
    public langc_ElementReference getLangc_elementreference() {
        return langc_elementreference;
    }

    public void setLangc_elementreference(langc_ElementReference langc_elementreference) {
        this.langc_elementreference = langc_elementreference;
    }
    public langc_Macro getLangc_macro() {
        return langc_macro;
    }

    public void setLangc_macro(langc_Macro langc_macro) {
        this.langc_macro = langc_macro;
    }
    public langc_ElementReference getLangc_elementreference() {
        return langc_elementreference;
    }

    public void setLangc_elementreference(langc_ElementReference langc_elementreference) {
        this.langc_elementreference = langc_elementreference;
    }
    public langc_BinaryOperation getLangc_binaryoperation() {
        return langc_binaryoperation;
    }

    public void setLangc_binaryoperation(langc_BinaryOperation langc_binaryoperation) {
        this.langc_binaryoperation = langc_binaryoperation;
    }

}