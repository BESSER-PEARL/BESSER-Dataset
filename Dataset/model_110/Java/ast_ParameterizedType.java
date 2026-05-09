





import java.util.List;
import java.util.ArrayList;

public class ast_ParameterizedType extends Type {






    private List<ast_Type> ast_types;




    private ast_Type ast_type;


    public ast_ParameterizedType(
    ) {
        super(
        );
        this.ast_types = new ArrayList<>();
    }

    public ast_ParameterizedType(
        ArrayList<ast_Type> ast_types    ) {
        this.ast_types = ast_types;
    }


    public List<ast_Type> getAst_types() {
        return ast_types;
    }

    public void addAst_type(Ast_type ast_type) {
        this.ast_types.add(ast_type);
    }
    public ast_Type getAst_type() {
        return ast_type;
    }

    public void setAst_type(ast_Type ast_type) {
        this.ast_type = ast_type;
    }

}