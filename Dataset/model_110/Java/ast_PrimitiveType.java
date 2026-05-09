





import java.util.List;
import java.util.ArrayList;

public class ast_PrimitiveType extends AnnotatableType {

    private String primitiveTypeCode;





    private List<ast_Annotation> ast_annotations;


    public ast_PrimitiveType(
        String primitiveTypeCode    ) {
        super(
        );
        this.primitiveTypeCode = primitiveTypeCode;
        this.ast_annotations = new ArrayList<>();
    }

    public ast_PrimitiveType(
        String primitiveTypeCode        ArrayList<ast_Annotation> ast_annotations    ) {
        this.primitiveTypeCode = primitiveTypeCode;
        this.ast_annotations = ast_annotations;
    }

    public String getPrimitivetypecode() {
        return primitiveTypeCode;
    }

    public void setPrimitivetypecode(String primitiveTypeCode) {
        this.primitiveTypeCode = primitiveTypeCode;
    }

    public List<ast_Annotation> getAst_annotations() {
        return ast_annotations;
    }

    public void addAst_annotation(Ast_annotation ast_annotation) {
        this.ast_annotations.add(ast_annotation);
    }

}