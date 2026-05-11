





import java.util.List;
import java.util.ArrayList;

public class ast_Definition  {

    private String name;





    private ast_Module ast_module;


    public ast_Definition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ast_Module getAst_module() {
        return ast_module;
    }

    public void setAst_module(ast_Module ast_module) {
        this.ast_module = ast_module;
    }

}