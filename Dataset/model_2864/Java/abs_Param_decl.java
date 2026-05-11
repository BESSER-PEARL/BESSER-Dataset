





import java.util.List;
import java.util.ArrayList;

public class abs_Param_decl extends Delta_param {

    private String name;





    private abs_Param_list abs_param_list;


    public abs_Param_decl(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public abs_Param_list getAbs_param_list() {
        return abs_param_list;
    }

    public void setAbs_param_list(abs_Param_list abs_param_list) {
        this.abs_param_list = abs_param_list;
    }

}