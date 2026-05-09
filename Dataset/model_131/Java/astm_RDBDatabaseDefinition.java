





import java.util.List;
import java.util.ArrayList;

public class astm_RDBDatabaseDefinition extends Definition {






    private List<astm_RDBTableSpaceReference> astm_rdbtablespacereferences;


    public astm_RDBDatabaseDefinition(
    ) {
        super(
        );
        this.astm_rdbtablespacereferences = new ArrayList<>();
    }

    public astm_RDBDatabaseDefinition(
        ArrayList<astm_RDBTableSpaceReference> astm_rdbtablespacereferences    ) {
        this.astm_rdbtablespacereferences = astm_rdbtablespacereferences;
    }


    public List<astm_RDBTableSpaceReference> getAstm_rdbtablespacereferences() {
        return astm_rdbtablespacereferences;
    }

    public void addAstm_rdbtablespacereference(Astm_rdbtablespacereference astm_rdbtablespacereference) {
        this.astm_rdbtablespacereferences.add(astm_rdbtablespacereference);
    }

}