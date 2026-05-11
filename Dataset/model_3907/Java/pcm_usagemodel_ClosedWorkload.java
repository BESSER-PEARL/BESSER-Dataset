





import java.util.List;
import java.util.ArrayList;

public class pcm_usagemodel_ClosedWorkload extends Workload {

    private int population;



    public pcm_usagemodel_ClosedWorkload(
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


}