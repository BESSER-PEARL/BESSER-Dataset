





import java.util.List;
import java.util.ArrayList;

public class qvtrelationcs_TopLevelCS extends RootPackageCS {






    private List<qvtrelationcs_UnitCS> qvtrelationcs_unitcss;


    public qvtrelationcs_TopLevelCS(
    ) {
        super(
        );
        this.qvtrelationcs_unitcss = new ArrayList<>();
    }

    public qvtrelationcs_TopLevelCS(
        ArrayList<qvtrelationcs_UnitCS> qvtrelationcs_unitcss    ) {
        this.qvtrelationcs_unitcss = qvtrelationcs_unitcss;
    }


    public List<qvtrelationcs_UnitCS> getQvtrelationcs_unitcss() {
        return qvtrelationcs_unitcss;
    }

    public void addQvtrelationcs_unitcs(Qvtrelationcs_unitcs qvtrelationcs_unitcs) {
        this.qvtrelationcs_unitcss.add(qvtrelationcs_unitcs);
    }

}