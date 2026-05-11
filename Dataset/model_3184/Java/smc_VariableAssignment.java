





import java.util.List;
import java.util.ArrayList;

public class smc_VariableAssignment extends Command {






    private smc_AbstractAssignment smc_abstractassignment;




    private smc_VariableDecl smc_variabledecl;


    public smc_VariableAssignment(
    ) {
        super(
        );
    }



    public smc_AbstractAssignment getSmc_abstractassignment() {
        return smc_abstractassignment;
    }

    public void setSmc_abstractassignment(smc_AbstractAssignment smc_abstractassignment) {
        this.smc_abstractassignment = smc_abstractassignment;
    }
    public smc_VariableDecl getSmc_variabledecl() {
        return smc_variabledecl;
    }

    public void setSmc_variabledecl(smc_VariableDecl smc_variabledecl) {
        this.smc_variabledecl = smc_variabledecl;
    }

}