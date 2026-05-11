





import java.util.List;
import java.util.ArrayList;

public class pascal_var_list  {

    private String var_type;
    private String var_ids;
    private String var_id;



    public pascal_var_list(
        String var_type,        String var_ids,        String var_id    ) {
        this.var_type = var_type;
        this.var_ids = var_ids;
        this.var_id = var_id;
    }


    public String getVar_type() {
        return var_type;
    }

    public void setVar_type(String var_type) {
        this.var_type = var_type;
    }
    public String getVar_ids() {
        return var_ids;
    }

    public void setVar_ids(String var_ids) {
        this.var_ids = var_ids;
    }
    public String getVar_id() {
        return var_id;
    }

    public void setVar_id(String var_id) {
        this.var_id = var_id;
    }


}