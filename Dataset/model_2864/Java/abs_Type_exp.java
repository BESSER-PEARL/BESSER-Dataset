





import java.util.List;
import java.util.ArrayList;

public class abs_Type_exp extends Update_preamble_declaration {

    private String name;





    private abs_Param_decl abs_param_decl;




    private List<abs_Type_use> abs_type_uses;


    public abs_Type_exp(
        String name    ) {
        super(
        );
        this.name = name;
        this.abs_type_uses = new ArrayList<>();
    }

    public abs_Type_exp(
        String name        ArrayList<abs_Type_use> abs_type_uses    ) {
        this.name = name;
        this.abs_type_uses = abs_type_uses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public abs_Param_decl getAbs_param_decl() {
        return abs_param_decl;
    }

    public void setAbs_param_decl(abs_Param_decl abs_param_decl) {
        this.abs_param_decl = abs_param_decl;
    }
    public List<abs_Type_use> getAbs_type_uses() {
        return abs_type_uses;
    }

    public void addAbs_type_use(Abs_type_use abs_type_use) {
        this.abs_type_uses.add(abs_type_use);
    }

}