





import java.util.List;
import java.util.ArrayList;

public class pascal_var_decl  {

    private String var_type;
    private String value;
    private String var_id;



    public pascal_var_decl(
        String var_type,        String value,        String var_id    ) {
        this.var_type = var_type;
        this.value = value;
        this.var_id = var_id;
    }


    public String getVar_type() {
        return var_type;
    }

    public void setVar_type(String var_type) {
        this.var_type = var_type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getVar_id() {
        return var_id;
    }

    public void setVar_id(String var_id) {
        this.var_id = var_id;
    }


}