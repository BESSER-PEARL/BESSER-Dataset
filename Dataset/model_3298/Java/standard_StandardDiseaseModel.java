





import java.util.List;
import java.util.ArrayList;

public class standard_StandardDiseaseModel extends DiseaseModel, IntegrationDecorator {

    private float totalArea;
    private float referencePopulationDensity;
    private float totalPopulationCountReciprocal;
    private float totalPopulationCount;





    private standard_Infector standard_infector;


    public standard_StandardDiseaseModel(
        float totalArea,        float referencePopulationDensity,        float totalPopulationCountReciprocal,        float totalPopulationCount    ) {
        super(
        );
        this.totalArea = totalArea;
        this.referencePopulationDensity = referencePopulationDensity;
        this.totalPopulationCountReciprocal = totalPopulationCountReciprocal;
        this.totalPopulationCount = totalPopulationCount;
    }


    public float getTotalarea() {
        return totalArea;
    }

    public void setTotalarea(float totalArea) {
        this.totalArea = totalArea;
    }
    public float getReferencepopulationdensity() {
        return referencePopulationDensity;
    }

    public void setReferencepopulationdensity(float referencePopulationDensity) {
        this.referencePopulationDensity = referencePopulationDensity;
    }
    public float getTotalpopulationcountreciprocal() {
        return totalPopulationCountReciprocal;
    }

    public void setTotalpopulationcountreciprocal(float totalPopulationCountReciprocal) {
        this.totalPopulationCountReciprocal = totalPopulationCountReciprocal;
    }
    public float getTotalpopulationcount() {
        return totalPopulationCount;
    }

    public void setTotalpopulationcount(float totalPopulationCount) {
        this.totalPopulationCount = totalPopulationCount;
    }

    public standard_Infector getStandard_infector() {
        return standard_infector;
    }

    public void setStandard_infector(standard_Infector standard_infector) {
        this.standard_infector = standard_infector;
    }

}