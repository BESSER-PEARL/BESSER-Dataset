





import java.util.List;
import java.util.ArrayList;

public class ast_Dimension extends ASTNode {






    private List<ast_Annotation> ast_annotations;


    public ast_Dimension(
    ) {
        super(
        );
        this.ast_annotations = new ArrayList<>();
    }

    public ast_Dimension(
        ArrayList<ast_Annotation> ast_annotations    ) {
        this.ast_annotations = ast_annotations;
    }


    public List<ast_Annotation> getAst_annotations() {
        return ast_annotations;
    }

    public void addAst_annotation(Ast_annotation ast_annotation) {
        this.ast_annotations.add(ast_annotation);
    }

}