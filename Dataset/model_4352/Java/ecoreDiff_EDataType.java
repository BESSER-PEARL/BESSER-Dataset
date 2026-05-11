





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EDataType extends EClassifier {

    private boolean serializable;





    private ecoreDiff_ChangedEDataType ecorediff_changededatatype;


    public ecoreDiff_EDataType(
        boolean serializable    ) {
        super(
        );
        this.serializable = serializable;
    }


    public boolean getSerializable() {
        return serializable;
    }

    public void setSerializable(boolean serializable) {
        this.serializable = serializable;
    }

    public ecoreDiff_ChangedEDataType getEcorediff_changededatatype() {
        return ecorediff_changededatatype;
    }

    public void setEcorediff_changededatatype(ecoreDiff_ChangedEDataType ecorediff_changededatatype) {
        this.ecorediff_changededatatype = ecorediff_changededatatype;
    }

}