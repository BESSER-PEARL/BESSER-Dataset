





import java.util.List;
import java.util.ArrayList;

public class smc_CreateTable extends Functions {






    private List<smc_ParamDecl> smc_paramdecls;




    private smc_VariableDecl smc_variabledecl;


    public smc_CreateTable(
    ) {
        super(
        );
        this.smc_paramdecls = new ArrayList<>();
    }

    public smc_CreateTable(
        ArrayList<smc_ParamDecl> smc_paramdecls    ) {
        this.smc_paramdecls = smc_paramdecls;
    }


    public List<smc_ParamDecl> getSmc_paramdecls() {
        return smc_paramdecls;
    }

    public void addSmc_paramdecl(Smc_paramdecl smc_paramdecl) {
        this.smc_paramdecls.add(smc_paramdecl);
    }
    public smc_VariableDecl getSmc_variabledecl() {
        return smc_variabledecl;
    }

    public void setSmc_variabledecl(smc_VariableDecl smc_variabledecl) {
        this.smc_variabledecl = smc_variabledecl;
    }

}