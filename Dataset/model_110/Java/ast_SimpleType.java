





import java.util.List;
import java.util.ArrayList;

public class ast_SimpleType extends AnnotatableType {






    private ast_Name ast_name;




    private List<ast_Annotation> ast_annotations;


    public ast_SimpleType(
    ) {
        super(
        );
        this.ast_annotations = new ArrayList<>();
    }

    public ast_SimpleType(
        ArrayList<ast_Annotation> ast_annotations    ) {
        this.ast_annotations = ast_annotations;
    }


    public ast_Name getAst_name() {
        return ast_name;
    }

    public void setAst_name(ast_Name ast_name) {
        this.ast_name = ast_name;
    }
    public List<ast_Annotation> getAst_annotations() {
        return ast_annotations;
    }

    public void addAst_annotation(Ast_annotation ast_annotation) {
        this.ast_annotations.add(ast_annotation);
    }

}