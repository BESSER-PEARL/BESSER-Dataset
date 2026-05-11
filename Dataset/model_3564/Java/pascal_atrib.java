





import java.util.List;
import java.util.ArrayList;

public class pascal_atrib  {

    private String var_id;





    private pascal_statement pascal_statement;


    public pascal_atrib(
        String var_id    ) {
        this.var_id = var_id;
    }


    public String getVar_id() {
        return var_id;
    }

    public void setVar_id(String var_id) {
        this.var_id = var_id;
    }

    public pascal_statement getPascal_statement() {
        return pascal_statement;
    }

    public void setPascal_statement(pascal_statement pascal_statement) {
        this.pascal_statement = pascal_statement;
    }

}