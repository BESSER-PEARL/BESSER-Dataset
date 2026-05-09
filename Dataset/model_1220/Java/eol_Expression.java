





import java.util.List;
import java.util.ArrayList;

public class eol_Expression  {

    private boolean inBrackets;





    private eol_AssignmentStatement eol_assignmentstatement;




    private eol_ExecutableAnnotationStatement eol_executableannotationstatement;




    private eol_Type eol_type;




    private eol_ExpressionRange eol_expressionrange;




    private eol_ExpressionRange eol_expressionrange;




    private eol_SwitchStatement eol_switchstatement;




    private eol_ReturnStatement eol_returnstatement;




    private eol_ExpressionList eol_expressionlist;




    private eol_ExpressionStatement eol_expressionstatement;




    private eol_ExpressionOrStatementBlock eol_expressionorstatementblock;




    private eol_IfStatement eol_ifstatement;




    private eol_SwitchCaseExpressionStatement eol_switchcaseexpressionstatement;




    private eol_ThrowStatement eol_throwstatement;




    private eol_DeleteStatement eol_deletestatement;




    private eol_ForStatement eol_forstatement;




    private eol_ExpressionOrStatementBlock eol_expressionorstatementblock;




    private eol_WhileStatement eol_whilestatement;




    private eol_AssignmentStatement eol_assignmentstatement;




    private eol_FOLMethodCallExpression eol_folmethodcallexpression;


    public eol_Expression(
        boolean inBrackets    ) {
        this.inBrackets = inBrackets;
    }


    public boolean getInbrackets() {
        return inBrackets;
    }

    public void setInbrackets(boolean inBrackets) {
        this.inBrackets = inBrackets;
    }

    public eol_AssignmentStatement getEol_assignmentstatement() {
        return eol_assignmentstatement;
    }

    public void setEol_assignmentstatement(eol_AssignmentStatement eol_assignmentstatement) {
        this.eol_assignmentstatement = eol_assignmentstatement;
    }
    public eol_ExecutableAnnotationStatement getEol_executableannotationstatement() {
        return eol_executableannotationstatement;
    }

    public void setEol_executableannotationstatement(eol_ExecutableAnnotationStatement eol_executableannotationstatement) {
        this.eol_executableannotationstatement = eol_executableannotationstatement;
    }
    public eol_Type getEol_type() {
        return eol_type;
    }

    public void setEol_type(eol_Type eol_type) {
        this.eol_type = eol_type;
    }
    public eol_ExpressionRange getEol_expressionrange() {
        return eol_expressionrange;
    }

    public void setEol_expressionrange(eol_ExpressionRange eol_expressionrange) {
        this.eol_expressionrange = eol_expressionrange;
    }
    public eol_ExpressionRange getEol_expressionrange() {
        return eol_expressionrange;
    }

    public void setEol_expressionrange(eol_ExpressionRange eol_expressionrange) {
        this.eol_expressionrange = eol_expressionrange;
    }
    public eol_SwitchStatement getEol_switchstatement() {
        return eol_switchstatement;
    }

    public void setEol_switchstatement(eol_SwitchStatement eol_switchstatement) {
        this.eol_switchstatement = eol_switchstatement;
    }
    public eol_ReturnStatement getEol_returnstatement() {
        return eol_returnstatement;
    }

    public void setEol_returnstatement(eol_ReturnStatement eol_returnstatement) {
        this.eol_returnstatement = eol_returnstatement;
    }
    public eol_ExpressionList getEol_expressionlist() {
        return eol_expressionlist;
    }

    public void setEol_expressionlist(eol_ExpressionList eol_expressionlist) {
        this.eol_expressionlist = eol_expressionlist;
    }
    public eol_ExpressionStatement getEol_expressionstatement() {
        return eol_expressionstatement;
    }

    public void setEol_expressionstatement(eol_ExpressionStatement eol_expressionstatement) {
        this.eol_expressionstatement = eol_expressionstatement;
    }
    public eol_ExpressionOrStatementBlock getEol_expressionorstatementblock() {
        return eol_expressionorstatementblock;
    }

    public void setEol_expressionorstatementblock(eol_ExpressionOrStatementBlock eol_expressionorstatementblock) {
        this.eol_expressionorstatementblock = eol_expressionorstatementblock;
    }
    public eol_IfStatement getEol_ifstatement() {
        return eol_ifstatement;
    }

    public void setEol_ifstatement(eol_IfStatement eol_ifstatement) {
        this.eol_ifstatement = eol_ifstatement;
    }
    public eol_SwitchCaseExpressionStatement getEol_switchcaseexpressionstatement() {
        return eol_switchcaseexpressionstatement;
    }

    public void setEol_switchcaseexpressionstatement(eol_SwitchCaseExpressionStatement eol_switchcaseexpressionstatement) {
        this.eol_switchcaseexpressionstatement = eol_switchcaseexpressionstatement;
    }
    public eol_ThrowStatement getEol_throwstatement() {
        return eol_throwstatement;
    }

    public void setEol_throwstatement(eol_ThrowStatement eol_throwstatement) {
        this.eol_throwstatement = eol_throwstatement;
    }
    public eol_DeleteStatement getEol_deletestatement() {
        return eol_deletestatement;
    }

    public void setEol_deletestatement(eol_DeleteStatement eol_deletestatement) {
        this.eol_deletestatement = eol_deletestatement;
    }
    public eol_ForStatement getEol_forstatement() {
        return eol_forstatement;
    }

    public void setEol_forstatement(eol_ForStatement eol_forstatement) {
        this.eol_forstatement = eol_forstatement;
    }
    public eol_ExpressionOrStatementBlock getEol_expressionorstatementblock() {
        return eol_expressionorstatementblock;
    }

    public void setEol_expressionorstatementblock(eol_ExpressionOrStatementBlock eol_expressionorstatementblock) {
        this.eol_expressionorstatementblock = eol_expressionorstatementblock;
    }
    public eol_WhileStatement getEol_whilestatement() {
        return eol_whilestatement;
    }

    public void setEol_whilestatement(eol_WhileStatement eol_whilestatement) {
        this.eol_whilestatement = eol_whilestatement;
    }
    public eol_AssignmentStatement getEol_assignmentstatement() {
        return eol_assignmentstatement;
    }

    public void setEol_assignmentstatement(eol_AssignmentStatement eol_assignmentstatement) {
        this.eol_assignmentstatement = eol_assignmentstatement;
    }
    public eol_FOLMethodCallExpression getEol_folmethodcallexpression() {
        return eol_folmethodcallexpression;
    }

    public void setEol_folmethodcallexpression(eol_FOLMethodCallExpression eol_folmethodcallexpression) {
        this.eol_folmethodcallexpression = eol_folmethodcallexpression;
    }

}