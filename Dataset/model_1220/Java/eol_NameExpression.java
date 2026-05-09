





import java.util.List;
import java.util.ArrayList;

public class eol_NameExpression extends Expression {

    private String resolvedContent;
    private String name;
    private boolean isType;





    private eol_AnnotationStatement eol_annotationstatement;




    private eol_TransactionStatement eol_transactionstatement;




    private eol_FOLMethodCallExpression eol_folmethodcallexpression;




    private eol_EnumerationLiteralExpression eol_enumerationliteralexpression;




    private eol_ModelDeclarationStatement eol_modeldeclarationstatement;




    private eol_EnumerationLiteralExpression eol_enumerationliteralexpression;




    private eol_OperationDefinition eol_operationdefinition;




    private eol_EnumerationLiteralExpression eol_enumerationliteralexpression;


    public eol_NameExpression(
        String resolvedContent,        String name,        boolean isType    ) {
        super(
        );
        this.resolvedContent = resolvedContent;
        this.name = name;
        this.isType = isType;
    }


    public String getResolvedcontent() {
        return resolvedContent;
    }

    public void setResolvedcontent(String resolvedContent) {
        this.resolvedContent = resolvedContent;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIstype() {
        return isType;
    }

    public void setIstype(boolean isType) {
        this.isType = isType;
    }

    public eol_AnnotationStatement getEol_annotationstatement() {
        return eol_annotationstatement;
    }

    public void setEol_annotationstatement(eol_AnnotationStatement eol_annotationstatement) {
        this.eol_annotationstatement = eol_annotationstatement;
    }
    public eol_TransactionStatement getEol_transactionstatement() {
        return eol_transactionstatement;
    }

    public void setEol_transactionstatement(eol_TransactionStatement eol_transactionstatement) {
        this.eol_transactionstatement = eol_transactionstatement;
    }
    public eol_FOLMethodCallExpression getEol_folmethodcallexpression() {
        return eol_folmethodcallexpression;
    }

    public void setEol_folmethodcallexpression(eol_FOLMethodCallExpression eol_folmethodcallexpression) {
        this.eol_folmethodcallexpression = eol_folmethodcallexpression;
    }
    public eol_EnumerationLiteralExpression getEol_enumerationliteralexpression() {
        return eol_enumerationliteralexpression;
    }

    public void setEol_enumerationliteralexpression(eol_EnumerationLiteralExpression eol_enumerationliteralexpression) {
        this.eol_enumerationliteralexpression = eol_enumerationliteralexpression;
    }
    public eol_ModelDeclarationStatement getEol_modeldeclarationstatement() {
        return eol_modeldeclarationstatement;
    }

    public void setEol_modeldeclarationstatement(eol_ModelDeclarationStatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatement = eol_modeldeclarationstatement;
    }
    public eol_EnumerationLiteralExpression getEol_enumerationliteralexpression() {
        return eol_enumerationliteralexpression;
    }

    public void setEol_enumerationliteralexpression(eol_EnumerationLiteralExpression eol_enumerationliteralexpression) {
        this.eol_enumerationliteralexpression = eol_enumerationliteralexpression;
    }
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
    }
    public eol_EnumerationLiteralExpression getEol_enumerationliteralexpression() {
        return eol_enumerationliteralexpression;
    }

    public void setEol_enumerationliteralexpression(eol_EnumerationLiteralExpression eol_enumerationliteralexpression) {
        this.eol_enumerationliteralexpression = eol_enumerationliteralexpression;
    }

}