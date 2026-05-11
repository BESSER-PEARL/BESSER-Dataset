





import java.util.List;
import java.util.ArrayList;

public class smc_Expression extends AbstractAssignment {






    private smc_IfThenElse smc_ifthenelse;




    private smc_While smc_while;




    private smc_Print smc_print;


    public smc_Expression(
    ) {
        super(
        );
    }



    public smc_IfThenElse getSmc_ifthenelse() {
        return smc_ifthenelse;
    }

    public void setSmc_ifthenelse(smc_IfThenElse smc_ifthenelse) {
        this.smc_ifthenelse = smc_ifthenelse;
    }
    public smc_While getSmc_while() {
        return smc_while;
    }

    public void setSmc_while(smc_While smc_while) {
        this.smc_while = smc_while;
    }
    public smc_Print getSmc_print() {
        return smc_print;
    }

    public void setSmc_print(smc_Print smc_print) {
        this.smc_print = smc_print;
    }

}