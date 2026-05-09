





import java.util.List;
import java.util.ArrayList;

public class ast_IntersectionType extends Type {






    private List<ast_Type> ast_types;


    public ast_IntersectionType(
    ) {
        super(
        );
        this.ast_types = new ArrayList<>();
    }

    public ast_IntersectionType(
        ArrayList<ast_Type> ast_types    ) {
        this.ast_types = ast_types;
    }


    public List<ast_Type> getAst_types() {
        return ast_types;
    }

    public void addAst_type(Ast_type ast_type) {
        this.ast_types.add(ast_type);
    }

}