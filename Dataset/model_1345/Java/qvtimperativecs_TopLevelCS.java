





import java.util.List;
import java.util.ArrayList;

public class qvtimperativecs_TopLevelCS extends RootPackageCS {






    private List<qvtimperativecs_MappingCS> qvtimperativecs_mappingcss;


    public qvtimperativecs_TopLevelCS(
    ) {
        super(
        );
        this.qvtimperativecs_mappingcss = new ArrayList<>();
    }

    public qvtimperativecs_TopLevelCS(
        ArrayList<qvtimperativecs_MappingCS> qvtimperativecs_mappingcss    ) {
        this.qvtimperativecs_mappingcss = qvtimperativecs_mappingcss;
    }


    public List<qvtimperativecs_MappingCS> getQvtimperativecs_mappingcss() {
        return qvtimperativecs_mappingcss;
    }

    public void addQvtimperativecs_mappingcs(Qvtimperativecs_mappingcs qvtimperativecs_mappingcs) {
        this.qvtimperativecs_mappingcss.add(qvtimperativecs_mappingcs);
    }

}