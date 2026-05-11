





import java.util.List;
import java.util.ArrayList;

public class smm_MeasureLibrary extends SmmElement {






    private List<smm_AbstractMeasureElement> smm_abstractmeasureelements;




    private smm_SmmModel smm_smmmodel;


    public smm_MeasureLibrary(
    ) {
        super(
        );
        this.smm_abstractmeasureelements = new ArrayList<>();
    }

    public smm_MeasureLibrary(
        ArrayList<smm_AbstractMeasureElement> smm_abstractmeasureelements    ) {
        this.smm_abstractmeasureelements = smm_abstractmeasureelements;
    }


    public List<smm_AbstractMeasureElement> getSmm_abstractmeasureelements() {
        return smm_abstractmeasureelements;
    }

    public void addSmm_abstractmeasureelement(Smm_abstractmeasureelement smm_abstractmeasureelement) {
        this.smm_abstractmeasureelements.add(smm_abstractmeasureelement);
    }
    public smm_SmmModel getSmm_smmmodel() {
        return smm_smmmodel;
    }

    public void setSmm_smmmodel(smm_SmmModel smm_smmmodel) {
        this.smm_smmmodel = smm_smmmodel;
    }

}