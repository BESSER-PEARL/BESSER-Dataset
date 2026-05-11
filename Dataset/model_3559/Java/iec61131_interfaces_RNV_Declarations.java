





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_RNV_Declarations extends Other_Var_Declaration {






    private List<Var_Init_Decl> var_init_decls;


    public iec61131_interfaces_RNV_Declarations(
    ) {
        super(
        );
        this.var_init_decls = new ArrayList<>();
    }

    public iec61131_interfaces_RNV_Declarations(
        ArrayList<Var_Init_Decl> var_init_decls    ) {
        this.var_init_decls = var_init_decls;
    }


    public List<Var_Init_Decl> getVar_init_decls() {
        return var_init_decls;
    }

    public void addVar_init_decl(Var_init_decl var_init_decl) {
        this.var_init_decls.add(var_init_decl);
    }

}