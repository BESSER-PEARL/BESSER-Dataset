





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload extends Workload {

    private int population;





    private PCMRandomVariable pcmrandomvariable;


    public pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload(
        int population    ) {
        super(
        );
        this.population = population;
    }


    public int getPopulation() {
        return population;
    }

    public void setPopulation(int population) {
        this.population = population;
    }

    public PCMRandomVariable getPcmrandomvariable() {
        return pcmrandomvariable;
    }

    public void setPcmrandomvariable(PCMRandomVariable pcmrandomvariable) {
        this.pcmrandomvariable = pcmrandomvariable;
    }

}