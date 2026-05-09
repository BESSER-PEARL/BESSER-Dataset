





import java.util.List;
import java.util.ArrayList;

public class eol_OperationDefinition extends EolElement {






    private eol_AnnotationBlock eol_annotationblock;




    private eol_Type eol_type;




    private List<eol_FormalParameterExpression> eol_formalparameterexpressions;




    private eol_EolLibraryModule eol_eollibrarymodule;




    private eol_Block eol_block;




    private eol_Type eol_type;




    private eol_OperationDefinition eol_operationdefinition;


    public eol_OperationDefinition(
    ) {
        super(
        );
        this.eol_formalparameterexpressions = new ArrayList<>();
    }

    public eol_OperationDefinition(
        ArrayList<eol_FormalParameterExpression> eol_formalparameterexpressions    ) {
        this.eol_formalparameterexpressions = eol_formalparameterexpressions;
    }


    public eol_AnnotationBlock getEol_annotationblock() {
        return eol_annotationblock;
    }

    public void setEol_annotationblock(eol_AnnotationBlock eol_annotationblock) {
        this.eol_annotationblock = eol_annotationblock;
    }
    public eol_Type getEol_type() {
        return eol_type;
    }

    public void setEol_type(eol_Type eol_type) {
        this.eol_type = eol_type;
    }
    public List<eol_FormalParameterExpression> getEol_formalparameterexpressions() {
        return eol_formalparameterexpressions;
    }

    public void addEol_formalparameterexpression(Eol_formalparameterexpression eol_formalparameterexpression) {
        this.eol_formalparameterexpressions.add(eol_formalparameterexpression);
    }
    public eol_EolLibraryModule getEol_eollibrarymodule() {
        return eol_eollibrarymodule;
    }

    public void setEol_eollibrarymodule(eol_EolLibraryModule eol_eollibrarymodule) {
        this.eol_eollibrarymodule = eol_eollibrarymodule;
    }
    public eol_Block getEol_block() {
        return eol_block;
    }

    public void setEol_block(eol_Block eol_block) {
        this.eol_block = eol_block;
    }
    public eol_Type getEol_type() {
        return eol_type;
    }

    public void setEol_type(eol_Type eol_type) {
        this.eol_type = eol_type;
    }
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
    }

}