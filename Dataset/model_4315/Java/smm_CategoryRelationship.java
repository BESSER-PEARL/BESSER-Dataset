





import java.util.List;
import java.util.ArrayList;

public class smm_CategoryRelationship extends SmmRelationship {






    private smm_AbstractMeasureElement smm_abstractmeasureelement;




    private smm_MeasureLibrary smm_measurelibrary;


    public smm_CategoryRelationship(
    ) {
        super(
        );
    }



    public smm_AbstractMeasureElement getSmm_abstractmeasureelement() {
        return smm_abstractmeasureelement;
    }

    public void setSmm_abstractmeasureelement(smm_AbstractMeasureElement smm_abstractmeasureelement) {
        this.smm_abstractmeasureelement = smm_abstractmeasureelement;
    }
    public smm_MeasureLibrary getSmm_measurelibrary() {
        return smm_measurelibrary;
    }

    public void setSmm_measurelibrary(smm_MeasureLibrary smm_measurelibrary) {
        this.smm_measurelibrary = smm_measurelibrary;
    }

}