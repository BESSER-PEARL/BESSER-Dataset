





import java.util.List;
import java.util.ArrayList;

public class ast_WildcardType extends AnnotatableType {

    private boolean upperBound;





    private List<ast_Annotation> ast_annotations;




    private ast_Type ast_type;


    public ast_WildcardType(
        boolean upperBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.ast_annotations = new ArrayList<>();
    }

    public ast_WildcardType(
        boolean upperBound        ArrayList<ast_Annotation> ast_annotations    ) {
        this.upperBound = upperBound;
        this.ast_annotations = ast_annotations;
    }

    public boolean getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(boolean upperBound) {
        this.upperBound = upperBound;
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

}