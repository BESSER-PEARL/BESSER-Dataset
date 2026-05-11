





import java.util.List;
import java.util.ArrayList;

public class ctmc_State  {

    private String name;
    private float exitRate;





    private ctmc_CTMC ctmc_ctmc;


    public ctmc_State(
        String name,        float exitRate    ) {
        this.name = name;
        this.exitRate = exitRate;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getExitrate() {
        return exitRate;
    }

    public void setExitrate(float exitRate) {
        this.exitRate = exitRate;
    }

    public ctmc_CTMC getCtmc_ctmc() {
        return ctmc_ctmc;
    }

    public void setCtmc_ctmc(ctmc_CTMC ctmc_ctmc) {
        this.ctmc_ctmc = ctmc_ctmc;
    }

}