





import java.util.List;
import java.util.ArrayList;

public class abs_Methodsig extends Class_modifier_fragment, Interface_modifier_fragment {

    private String name;





    private abs_Has_condition abs_has_condition;




    private abs_Interface_decl abs_interface_decl;




    private abs_Param_list abs_param_list;




    private abs_Type_use abs_type_use;


    public abs_Methodsig(
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

    public abs_Has_condition getAbs_has_condition() {
        return abs_has_condition;
    }

    public void setAbs_has_condition(abs_Has_condition abs_has_condition) {
        this.abs_has_condition = abs_has_condition;
    }
    public abs_Interface_decl getAbs_interface_decl() {
        return abs_interface_decl;
    }

    public void setAbs_interface_decl(abs_Interface_decl abs_interface_decl) {
        this.abs_interface_decl = abs_interface_decl;
    }
    public abs_Param_list getAbs_param_list() {
        return abs_param_list;
    }

    public void setAbs_param_list(abs_Param_list abs_param_list) {
        this.abs_param_list = abs_param_list;
    }
    public abs_Type_use getAbs_type_use() {
        return abs_type_use;
    }

    public void setAbs_type_use(abs_Type_use abs_type_use) {
        this.abs_type_use = abs_type_use;
    }

}