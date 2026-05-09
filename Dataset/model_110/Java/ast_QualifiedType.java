





import java.util.List;
import java.util.ArrayList;

public class ast_QualifiedType extends AnnotatableType {






    private List<ast_Annotation> ast_annotations;




    private ast_Type ast_type;




    private ast_SimpleName ast_simplename;


    public ast_QualifiedType(
    ) {
        super(
        );
        this.ast_annotations = new ArrayList<>();
    }

    public ast_QualifiedType(
        ArrayList<ast_Annotation> ast_annotations    ) {
        this.ast_annotations = ast_annotations;
    }


    public List<ast_Annotation> getAst_annotations() {
        return ast_annotations;
    }

    public void addAst_annotation(Ast_annotation ast_annotation) {
        this.ast_annotations.add(ast_annotation);
    }
    public ast_Type getAst_type() {
        return ast_type;
    }

    public void setAst_type(ast_Type ast_type) {
        this.ast_type = ast_type;
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }

}