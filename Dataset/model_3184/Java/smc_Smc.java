





import java.util.List;
import java.util.ArrayList;

public class smc_Smc  {






    private smc_MainSMC smc_mainsmc;




    private List<smc_BlockSMC> smc_blocksmcs;


    public smc_Smc(
    ) {
        this.smc_blocksmcs = new ArrayList<>();
    }

    public smc_Smc(
        ArrayList<smc_BlockSMC> smc_blocksmcs    ) {
        this.smc_blocksmcs = smc_blocksmcs;
    }


    public smc_MainSMC getSmc_mainsmc() {
        return smc_mainsmc;
    }

    public void setSmc_mainsmc(smc_MainSMC smc_mainsmc) {
        this.smc_mainsmc = smc_mainsmc;
    }
    public List<smc_BlockSMC> getSmc_blocksmcs() {
        return smc_blocksmcs;
    }

    public void addSmc_blocksmc(Smc_blocksmc smc_blocksmc) {
        this.smc_blocksmcs.add(smc_blocksmc);
    }

}