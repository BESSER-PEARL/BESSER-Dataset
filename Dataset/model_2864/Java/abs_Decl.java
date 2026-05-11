





import java.util.List;
import java.util.ArrayList;

public class abs_Decl  {

    private String name;





    private abs_Module_decl abs_module_decl;


    public abs_Decl(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public abs_Module_decl getAbs_module_decl() {
        return abs_module_decl;
    }

    public void setAbs_module_decl(abs_Module_decl abs_module_decl) {
        this.abs_module_decl = abs_module_decl;
    }

}