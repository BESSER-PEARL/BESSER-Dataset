





import java.util.List;
import java.util.ArrayList;

public class express_FunctionExpression  {

    private String name;





    private List<express_LocalVar> express_localvars;




    private List<express_Statement> express_statements;




    private express_DataType express_datatype;


    public express_FunctionExpression(
        String name    ) {
        this.name = name;
        this.express_localvars = new ArrayList<>();
        this.express_statements = new ArrayList<>();
    }

    public express_FunctionExpression(
        String name        ArrayList<express_LocalVar> express_localvars,        ArrayList<express_Statement> express_statements    ) {
        this.name = name;
        this.express_localvars = express_localvars;
        this.express_statements = express_statements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<express_LocalVar> getExpress_localvars() {
        return express_localvars;
    }

    public void addExpress_localvar(Express_localvar express_localvar) {
        this.express_localvars.add(express_localvar);
    }
    public List<express_Statement> getExpress_statements() {
        return express_statements;
    }

    public void addExpress_statement(Express_statement express_statement) {
        this.express_statements.add(express_statement);
    }
    public express_DataType getExpress_datatype() {
        return express_datatype;
    }

    public void setExpress_datatype(express_DataType express_datatype) {
        this.express_datatype = express_datatype;
    }

}