





import java.util.List;
import java.util.ArrayList;

public class eol_OperationDefinition extends EOLElement {






    private eol_VariableDeclarationExpression eol_variabledeclarationexpression;




    private eol_FOLMethodCallExpression eol_folmethodcallexpression;




    private eol_Type eol_type;




    private eol_NameExpression eol_nameexpression;




    private List<eol_OperationDefinition> eol_operationdefinitions;




    private eol_Type eol_type;




    private eol_EOLLibraryModule eol_eollibrarymodule;




    private eol_MethodCallExpression eol_methodcallexpression;




    private eol_VariableDeclarationExpression eol_variabledeclarationexpression;




    private List<eol_FormalParameterExpression> eol_formalparameterexpressions;


    public eol_OperationDefinition(
    ) {
        super(
        );
        this.eol_operationdefinitions = new ArrayList<>();
        this.eol_formalparameterexpressions = new ArrayList<>();
    }

    public eol_OperationDefinition(
        ArrayList<eol_OperationDefinition> eol_operationdefinitions,        ArrayList<eol_FormalParameterExpression> eol_formalparameterexpressions    ) {
        this.eol_operationdefinitions = eol_operationdefinitions;
        this.eol_formalparameterexpressions = eol_formalparameterexpressions;
    }


    public eol_VariableDeclarationExpression getEol_variabledeclarationexpression() {
        return eol_variabledeclarationexpression;
    }

    public void setEol_variabledeclarationexpression(eol_VariableDeclarationExpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpression = eol_variabledeclarationexpression;
    }
    public eol_FOLMethodCallExpression getEol_folmethodcallexpression() {
        return eol_folmethodcallexpression;
    }

    public void setEol_folmethodcallexpression(eol_FOLMethodCallExpression eol_folmethodcallexpression) {
        this.eol_folmethodcallexpression = eol_folmethodcallexpression;
    }
    public eol_Type getEol_type() {
        return eol_type;
    }

    public void setEol_type(eol_Type eol_type) {
        this.eol_type = eol_type;
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public List<eol_OperationDefinition> getEol_operationdefinitions() {
        return eol_operationdefinitions;
    }

    public void addEol_operationdefinition(Eol_operationdefinition eol_operationdefinition) {
        this.eol_operationdefinitions.add(eol_operationdefinition);
    }
    public eol_Type getEol_type() {
        return eol_type;
    }

    public void setEol_type(eol_Type eol_type) {
        this.eol_type = eol_type;
    }
    public eol_EOLLibraryModule getEol_eollibrarymodule() {
        return eol_eollibrarymodule;
    }

    public void setEol_eollibrarymodule(eol_EOLLibraryModule eol_eollibrarymodule) {
        this.eol_eollibrarymodule = eol_eollibrarymodule;
    }
    public eol_MethodCallExpression getEol_methodcallexpression() {
        return eol_methodcallexpression;
    }

    public void setEol_methodcallexpression(eol_MethodCallExpression eol_methodcallexpression) {
        this.eol_methodcallexpression = eol_methodcallexpression;
    }
    public eol_VariableDeclarationExpression getEol_variabledeclarationexpression() {
        return eol_variabledeclarationexpression;
    }

    public void setEol_variabledeclarationexpression(eol_VariableDeclarationExpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpression = eol_variabledeclarationexpression;
    }
    public List<eol_FormalParameterExpression> getEol_formalparameterexpressions() {
        return eol_formalparameterexpressions;
    }

    public void addEol_formalparameterexpression(Eol_formalparameterexpression eol_formalparameterexpression) {
        this.eol_formalparameterexpressions.add(eol_formalparameterexpression);
    }

}