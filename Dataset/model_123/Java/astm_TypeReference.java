





import java.util.List;
import java.util.ArrayList;

public class astm_TypeReference extends Type {






    private astm_AnnotationExpression astm_annotationexpression;




    private astm_Definition astm_definition;




    private astm_Declaration astm_declaration;


    public astm_TypeReference(
    ) {
        super(
        );
    }



    public astm_AnnotationExpression getAstm_annotationexpression() {
        return astm_annotationexpression;
    }

    public void setAstm_annotationexpression(astm_AnnotationExpression astm_annotationexpression) {
        this.astm_annotationexpression = astm_annotationexpression;
    }
    public astm_Definition getAstm_definition() {
        return astm_definition;
    }

    public void setAstm_definition(astm_Definition astm_definition) {
        this.astm_definition = astm_definition;
    }
    public astm_Declaration getAstm_declaration() {
        return astm_declaration;
    }

    public void setAstm_declaration(astm_Declaration astm_declaration) {
        this.astm_declaration = astm_declaration;
    }

}