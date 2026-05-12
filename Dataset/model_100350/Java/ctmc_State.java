





import java.util.List;
import java.util.ArrayList;

public class ctmc_State extends IDBase {

    private float exitRate;
    private String name;





    private ctmc_CTMC ctmc_ctmc;




    private ctmc_CTMC ctmc_ctmc;


    public ctmc_State(
        float exitRate,        String name    ) {
        super(
        );
        this.exitRate = exitRate;
        this.name = name;
    }


    public float getExitrate() {
        return exitRate;
    }

    public void setExitrate(float exitRate) {
        this.exitRate = exitRate;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ctmc_CTMC getCtmc_ctmc() {
        return ctmc_ctmc;
    }

    public void setCtmc_ctmc(ctmc_CTMC ctmc_ctmc) {
        this.ctmc_ctmc = ctmc_ctmc;
    }
    public ctmc_CTMC getCtmc_ctmc() {
        return ctmc_ctmc;
    }

    public void setCtmc_ctmc(ctmc_CTMC ctmc_ctmc) {
        this.ctmc_ctmc = ctmc_ctmc;
    }

}