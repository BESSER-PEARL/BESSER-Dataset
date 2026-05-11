





import java.util.List;
import java.util.ArrayList;

public class smc_BellLapadula extends AccessControl {

    private String mode;





    private smc_VariableDecl smc_variabledecl;


    public smc_BellLapadula(
        String mode    ) {
        super(
        );
        this.mode = mode;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public smc_VariableDecl getSmc_variabledecl() {
        return smc_variabledecl;
    }

    public void setSmc_variabledecl(smc_VariableDecl smc_variabledecl) {
        this.smc_variabledecl = smc_variabledecl;
    }

}