





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Output_Declarations extends Io_Var_Declaration {

    private boolean retain;





    private List<Var_Init_Decl> var_init_decls;


    public iec61131_interfaces_Output_Declarations(
        boolean retain    ) {
        super(
        );
        this.retain = retain;
        this.var_init_decls = new ArrayList<>();
    }

    public iec61131_interfaces_Output_Declarations(
        boolean retain        ArrayList<Var_Init_Decl> var_init_decls    ) {
        this.retain = retain;
        this.var_init_decls = var_init_decls;
    }

    public boolean getRetain() {
        return retain;
    }

    public void setRetain(boolean retain) {
        this.retain = retain;
    }

    public List<Var_Init_Decl> getVar_init_decls() {
        return var_init_decls;
    }

    public void addVar_init_decl(Var_init_decl var_init_decl) {
        this.var_init_decls.add(var_init_decl);
    }

}