





import java.util.List;
import java.util.ArrayList;

public class ast_UnionType extends Type {






    private List<ast_Type> ast_types;


    public ast_UnionType(
    ) {
        super(
        );
        this.ast_types = new ArrayList<>();
    }

    public ast_UnionType(
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