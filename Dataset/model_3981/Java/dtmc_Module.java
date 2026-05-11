





import java.util.List;
import java.util.ArrayList;

public class dtmc_Module  {

    private boolean isAutonomous;





    private dtmc_Dtmc dtmc_dtmc;


    public dtmc_Module(
        boolean isAutonomous    ) {
        this.isAutonomous = isAutonomous;
    }


    public boolean getIsautonomous() {
        return isAutonomous;
    }

    public void setIsautonomous(boolean isAutonomous) {
        this.isAutonomous = isAutonomous;
    }

    public dtmc_Dtmc getDtmc_dtmc() {
        return dtmc_dtmc;
    }

    public void setDtmc_dtmc(dtmc_Dtmc dtmc_dtmc) {
        this.dtmc_dtmc = dtmc_dtmc;
    }

}