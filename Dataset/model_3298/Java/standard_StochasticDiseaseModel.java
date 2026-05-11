





import java.util.List;
import java.util.ArrayList;

public class standard_StochasticDiseaseModel extends DiseaseModel {

    private String randomGenerator;
    private String seed;



    public standard_StochasticDiseaseModel(
        String randomGenerator,        String seed    ) {
        super(
        );
        this.randomGenerator = randomGenerator;
        this.seed = seed;
    }


    public String getRandomgenerator() {
        return randomGenerator;
    }

    public void setRandomgenerator(String randomGenerator) {
        this.randomGenerator = randomGenerator;
    }
    public String getSeed() {
        return seed;
    }

    public void setSeed(String seed) {
        this.seed = seed;
    }


}