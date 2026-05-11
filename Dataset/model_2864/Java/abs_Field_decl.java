





import java.util.List;
import java.util.ArrayList;

public class abs_Field_decl extends Class_modifier_fragment {

    private String name;





    private abs_Class_decl abs_class_decl;




    private abs_Var_or_field_ref abs_var_or_field_ref;




    private abs_Pure_exp abs_pure_exp;




    private abs_Has_condition abs_has_condition;




    private abs_Type_use abs_type_use;


    public abs_Field_decl(
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

    public abs_Class_decl getAbs_class_decl() {
        return abs_class_decl;
    }

    public void setAbs_class_decl(abs_Class_decl abs_class_decl) {
        this.abs_class_decl = abs_class_decl;
    }
    public abs_Var_or_field_ref getAbs_var_or_field_ref() {
        return abs_var_or_field_ref;
    }

    public void setAbs_var_or_field_ref(abs_Var_or_field_ref abs_var_or_field_ref) {
        this.abs_var_or_field_ref = abs_var_or_field_ref;
    }
    public abs_Pure_exp getAbs_pure_exp() {
        return abs_pure_exp;
    }

    public void setAbs_pure_exp(abs_Pure_exp abs_pure_exp) {
        this.abs_pure_exp = abs_pure_exp;
    }
    public abs_Has_condition getAbs_has_condition() {
        return abs_has_condition;
    }

    public void setAbs_has_condition(abs_Has_condition abs_has_condition) {
        this.abs_has_condition = abs_has_condition;
    }
    public abs_Type_use getAbs_type_use() {
        return abs_type_use;
    }

    public void setAbs_type_use(abs_Type_use abs_type_use) {
        this.abs_type_use = abs_type_use;
    }

}