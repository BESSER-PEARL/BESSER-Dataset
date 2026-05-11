





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEStringToStringMapEntry extends EStringToStringMapEntry {






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


    public List<ecoreDiff_EStringToStringMapEntry> getEcorediff_estringtostringmapentrys() {
        return ecorediff_estringtostringmapentrys;
    }

    public void addEcorediff_estringtostringmapentry(Ecorediff_estringtostringmapentry ecorediff_estringtostringmapentry) {
        this.ecorediff_estringtostringmapentrys.add(ecorediff_estringtostringmapentry);
    }

}