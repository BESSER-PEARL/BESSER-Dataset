





import java.util.List;
import java.util.ArrayList;

public class ast_SuperMethodReference extends MethodReference {






    private List<ast_Type> ast_types;




    private ast_Name ast_name;




    private ast_SimpleName ast_simplename;


    public ast_SuperMethodReference(
    ) {
        super(
        );
        this.ast_types = new ArrayList<>();
    }

    public ast_SuperMethodReference(
        ArrayList<ast_Type> ast_types    ) {
        this.ast_types = ast_types;
    }


    public List<ast_Type> getAst_types() {
        return ast_types;
    }

    public void addAst_type(Ast_type ast_type) {
        this.ast_types.add(ast_type);
    }
    public ast_Name getAst_name() {
        return ast_name;
    }

    public void setAst_name(ast_Name ast_name) {
        this.ast_name = ast_name;
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }

}