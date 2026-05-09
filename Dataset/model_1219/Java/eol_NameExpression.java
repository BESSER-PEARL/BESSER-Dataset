





import java.util.List;
import java.util.ArrayList;

public class eol_NameExpression extends Expression {

    private String resolvedContent;
    private String name;





    private eol_Annotation eol_annotation;




    private eol_TransactionStatement eol_transactionstatement;




    private eol_EolLibraryModule eol_eollibrarymodule;




    private eol_EnumerationLiteralExpression eol_enumerationliteralexpression;




    private eol_OperationDefinition eol_operationdefinition;




    private eol_EnumerationLiteralExpression eol_enumerationliteralexpression;




    private eol_ModelDeclarationParameter eol_modeldeclarationparameter;


    public eol_NameExpression(
        String resolvedContent,        String name    ) {
        super(
        );
        this.resolvedContent = resolvedContent;
        this.name = name;
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

    public eol_Annotation getEol_annotation() {
        return eol_annotation;
    }

    public void setEol_annotation(eol_Annotation eol_annotation) {
        this.eol_annotation = eol_annotation;
    }
    public eol_TransactionStatement getEol_transactionstatement() {
        return eol_transactionstatement;
    }

    public void setEol_transactionstatement(eol_TransactionStatement eol_transactionstatement) {
        this.eol_transactionstatement = eol_transactionstatement;
    }
    public eol_EolLibraryModule getEol_eollibrarymodule() {
        return eol_eollibrarymodule;
    }

    public void setEol_eollibrarymodule(eol_EolLibraryModule eol_eollibrarymodule) {
        this.eol_eollibrarymodule = eol_eollibrarymodule;
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
    public eol_ModelDeclarationParameter getEol_modeldeclarationparameter() {
        return eol_modeldeclarationparameter;
    }

    public void setEol_modeldeclarationparameter(eol_ModelDeclarationParameter eol_modeldeclarationparameter) {
        this.eol_modeldeclarationparameter = eol_modeldeclarationparameter;
    }

}