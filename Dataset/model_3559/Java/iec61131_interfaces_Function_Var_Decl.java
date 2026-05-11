





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Function_Var_Decl extends interfaces_Interface, pous_Function_Vars {

    private boolean constant;





    private List<Var2_Init_Decl> var2_init_decls;


    public iec61131_interfaces_Function_Var_Decl(
        boolean constant    ) {
        super(
        );
        this.constant = constant;
        this.var2_init_decls = new ArrayList<>();
    }

    public iec61131_interfaces_Function_Var_Decl(
        boolean constant        ArrayList<Var2_Init_Decl> var2_init_decls    ) {
        this.constant = constant;
        this.var2_init_decls = var2_init_decls;
    }

    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }

    public List<Var2_Init_Decl> getVar2_init_decls() {
        return var2_init_decls;
    }

    public void addVar2_init_decl(Var2_init_decl var2_init_decl) {
        this.var2_init_decls.add(var2_init_decl);
    }

}