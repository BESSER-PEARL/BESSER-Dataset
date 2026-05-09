





import java.util.List;
import java.util.ArrayList;

public class eol_FormalParameterExpression extends VariableDeclarationExpression {






    private eol_FOLMethodCallExpression eol_folmethodcallexpression;




    private eol_OperationDefinition eol_operationdefinition;




    private eol_ForStatement eol_forstatement;


    public eol_FormalParameterExpression(
    ) {
        super(
        );
    }



    public eol_FOLMethodCallExpression getEol_folmethodcallexpression() {
        return eol_folmethodcallexpression;
    }

    public void setEol_folmethodcallexpression(eol_FOLMethodCallExpression eol_folmethodcallexpression) {
        this.eol_folmethodcallexpression = eol_folmethodcallexpression;
    }
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
    }
    public eol_ForStatement getEol_forstatement() {
        return eol_forstatement;
    }

    public void setEol_forstatement(eol_ForStatement eol_forstatement) {
        this.eol_forstatement = eol_forstatement;
    }

}