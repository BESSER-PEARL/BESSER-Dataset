





import java.util.List;
import java.util.ArrayList;

public class astm_RDBUniqueKey extends RDBConstraint {






    private List<astm_RDBColumnReference> astm_rdbcolumnreferences;


    public astm_RDBUniqueKey(
    ) {
        super(
        );
        this.astm_rdbcolumnreferences = new ArrayList<>();
    }

    public astm_RDBUniqueKey(
        ArrayList<astm_RDBColumnReference> astm_rdbcolumnreferences    ) {
        this.astm_rdbcolumnreferences = astm_rdbcolumnreferences;
    }


    public List<astm_RDBColumnReference> getAstm_rdbcolumnreferences() {
        return astm_rdbcolumnreferences;
    }

    public void addAstm_rdbcolumnreference(Astm_rdbcolumnreference astm_rdbcolumnreference) {
        this.astm_rdbcolumnreferences.add(astm_rdbcolumnreference);
    }

}