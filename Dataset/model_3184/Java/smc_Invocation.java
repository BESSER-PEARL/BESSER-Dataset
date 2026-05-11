





import java.util.List;
import java.util.ArrayList;

public class smc_Invocation extends Expression {






    private smc_InvocationVoid smc_invocationvoid;




    private smc_BlockSMC smc_blocksmc;


    public smc_Invocation(
    ) {
        super(
        );
    }



    public smc_InvocationVoid getSmc_invocationvoid() {
        return smc_invocationvoid;
    }

    public void setSmc_invocationvoid(smc_InvocationVoid smc_invocationvoid) {
        this.smc_invocationvoid = smc_invocationvoid;
    }
    public smc_BlockSMC getSmc_blocksmc() {
        return smc_blocksmc;
    }

    public void setSmc_blocksmc(smc_BlockSMC smc_blocksmc) {
        this.smc_blocksmc = smc_blocksmc;
    }

}