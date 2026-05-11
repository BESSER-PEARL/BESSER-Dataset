





import java.util.List;
import java.util.ArrayList;

public class smm_MeasureLibrary extends SmmElement {






    private List<smm_AbstractMeasureElement> smm_abstractmeasureelements;


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

}