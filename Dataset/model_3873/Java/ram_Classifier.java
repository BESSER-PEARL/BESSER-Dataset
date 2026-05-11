





import java.util.List;
import java.util.ArrayList;

public class ram_Classifier extends ObjectType, Traceable {

    private boolean dataType;





    private ram_Classifier ram_classifier;


    public ram_Classifier(
        boolean dataType    ) {
        super(
        );
        this.dataType = dataType;
    }


    public boolean getDatatype() {
        return dataType;
    }

    public void setDatatype(boolean dataType) {
        this.dataType = dataType;
    }

    public ram_Classifier getRam_classifier() {
        return ram_classifier;
    }

    public void setRam_classifier(ram_Classifier ram_classifier) {
        this.ram_classifier = ram_classifier;
    }

}