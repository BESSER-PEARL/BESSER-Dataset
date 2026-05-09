





import java.util.List;
import java.util.ArrayList;

public class ast_ArrayType extends Type {






    private List<ast_Dimension> ast_dimensions;




    private ast_Type ast_type;




    private ast_ArrayCreation ast_arraycreation;


    public ast_ArrayType(
    ) {
        super(
        );
        this.ast_dimensions = new ArrayList<>();
    }

    public ast_ArrayType(
        ArrayList<ast_Dimension> ast_dimensions    ) {
        this.ast_dimensions = ast_dimensions;
    }


    public List<ast_Dimension> getAst_dimensions() {
        return ast_dimensions;
    }

    public void addAst_dimension(Ast_dimension ast_dimension) {
        this.ast_dimensions.add(ast_dimension);
    }
    public ast_Type getAst_type() {
        return ast_type;
    }

    public void setAst_type(ast_Type ast_type) {
        this.ast_type = ast_type;
    }
    public ast_ArrayCreation getAst_arraycreation() {
        return ast_arraycreation;
    }

    public void setAst_arraycreation(ast_ArrayCreation ast_arraycreation) {
        this.ast_arraycreation = ast_arraycreation;
    }

}