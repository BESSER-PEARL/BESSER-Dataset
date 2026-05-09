





import java.util.List;
import java.util.ArrayList;

public class astm_RDBTableDefinition extends Definition {






    private List<astm_RDBIndex> astm_rdbindexs;




    private List<astm_RDBTrigger> astm_rdbtriggers;




    private List<astm_RDBConstraint> astm_rdbconstraints;


    public astm_RDBTableDefinition(
    ) {
        super(
        );
        this.astm_rdbindexs = new ArrayList<>();
        this.astm_rdbtriggers = new ArrayList<>();
        this.astm_rdbconstraints = new ArrayList<>();
    }

    public astm_RDBTableDefinition(
        ArrayList<astm_RDBIndex> astm_rdbindexs,        ArrayList<astm_RDBTrigger> astm_rdbtriggers,        ArrayList<astm_RDBConstraint> astm_rdbconstraints    ) {
        this.astm_rdbindexs = astm_rdbindexs;
        this.astm_rdbtriggers = astm_rdbtriggers;
        this.astm_rdbconstraints = astm_rdbconstraints;
    }


    public List<astm_RDBIndex> getAstm_rdbindexs() {
        return astm_rdbindexs;
    }

    public void addAstm_rdbindex(Astm_rdbindex astm_rdbindex) {
        this.astm_rdbindexs.add(astm_rdbindex);
    }
    public List<astm_RDBTrigger> getAstm_rdbtriggers() {
        return astm_rdbtriggers;
    }

    public void addAstm_rdbtrigger(Astm_rdbtrigger astm_rdbtrigger) {
        this.astm_rdbtriggers.add(astm_rdbtrigger);
    }
    public List<astm_RDBConstraint> getAstm_rdbconstraints() {
        return astm_rdbconstraints;
    }

    public void addAstm_rdbconstraint(Astm_rdbconstraint astm_rdbconstraint) {
        this.astm_rdbconstraints.add(astm_rdbconstraint);
    }

}