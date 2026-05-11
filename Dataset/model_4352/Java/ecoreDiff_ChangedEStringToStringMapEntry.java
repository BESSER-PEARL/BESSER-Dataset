





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEStringToStringMapEntry extends EStringToStringMapEntry {






    private ecoreDiff_EObject ecorediff_eobject;




    private List<ecoreDiff_EStringToStringMapEntry> ecorediff_estringtostringmapentrys;


    public ecoreDiff_ChangedEStringToStringMapEntry(
    ) {
        super(
        );
        this.ecorediff_estringtostringmapentrys = new ArrayList<>();
    }

    public ecoreDiff_ChangedEStringToStringMapEntry(
        ArrayList<ecoreDiff_EStringToStringMapEntry> ecorediff_estringtostringmapentrys    ) {
        this.ecorediff_estringtostringmapentrys = ecorediff_estringtostringmapentrys;
    }


    public ecoreDiff_EObject getEcorediff_eobject() {
        return ecorediff_eobject;
    }

    public void setEcorediff_eobject(ecoreDiff_EObject ecorediff_eobject) {
        this.ecorediff_eobject = ecorediff_eobject;
    }
    public List<ecoreDiff_EStringToStringMapEntry> getEcorediff_estringtostringmapentrys() {
        return ecorediff_estringtostringmapentrys;
    }

    public void addEcorediff_estringtostringmapentry(Ecorediff_estringtostringmapentry ecorediff_estringtostringmapentry) {
        this.ecorediff_estringtostringmapentrys.add(ecorediff_estringtostringmapentry);
    }

}