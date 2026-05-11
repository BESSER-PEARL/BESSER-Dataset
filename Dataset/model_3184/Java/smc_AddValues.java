





import java.util.List;
import java.util.ArrayList;

public class smc_AddValues extends Functions {






    private smc_VariableDecl smc_variabledecl;




    private List<smc_VariableDecl> smc_variabledecls;


    public smc_AddValues(
    ) {
        super(
        );
        this.smc_variabledecls = new ArrayList<>();
    }

    public smc_AddValues(
        ArrayList<smc_VariableDecl> smc_variabledecls    ) {
        this.smc_variabledecls = smc_variabledecls;
    }


    public smc_VariableDecl getSmc_variabledecl() {
        return smc_variabledecl;
    }

    public void setSmc_variabledecl(smc_VariableDecl smc_variabledecl) {
        this.smc_variabledecl = smc_variabledecl;
    }
    public List<smc_VariableDecl> getSmc_variabledecls() {
        return smc_variabledecls;
    }

    public void addSmc_variabledecl(Smc_variabledecl smc_variabledecl) {
        this.smc_variabledecls.add(smc_variabledecl);
    }

}