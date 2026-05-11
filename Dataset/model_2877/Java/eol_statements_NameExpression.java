





import java.util.List;
import java.util.ArrayList;

public class eol_statements_NameExpression extends Expression {






    private eol_statements_AnnotationStatement eol_statements_annotationstatement;




    private eol_statements_ModelDeclarationStatement eol_statements_modeldeclarationstatement;


    public eol_statements_NameExpression(
    ) {
        super(
        );
    }



    public eol_statements_AnnotationStatement getEol_statements_annotationstatement() {
        return eol_statements_annotationstatement;
    }

    public void setEol_statements_annotationstatement(eol_statements_AnnotationStatement eol_statements_annotationstatement) {
        this.eol_statements_annotationstatement = eol_statements_annotationstatement;
    }
    public eol_statements_ModelDeclarationStatement getEol_statements_modeldeclarationstatement() {
        return eol_statements_modeldeclarationstatement;
    }

    public void setEol_statements_modeldeclarationstatement(eol_statements_ModelDeclarationStatement eol_statements_modeldeclarationstatement) {
        this.eol_statements_modeldeclarationstatement = eol_statements_modeldeclarationstatement;
    }

}