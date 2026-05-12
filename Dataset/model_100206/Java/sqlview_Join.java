





import java.util.List;
import java.util.ArrayList;

public class sqlview_Join  {






    private List<sqlview_JoinRight> sqlview_joinrights;




    private sqlview_From sqlview_from;




    private List<sqlview_JoinLeft> sqlview_joinlefts;




    private List<sqlview_Relation> sqlview_relations;


    public sqlview_Join(
    ) {
        this.sqlview_joinrights = new ArrayList<>();
        this.sqlview_joinlefts = new ArrayList<>();
        this.sqlview_relations = new ArrayList<>();
    }

    public sqlview_Join(
        ArrayList<sqlview_JoinRight> sqlview_joinrights,        ArrayList<sqlview_JoinLeft> sqlview_joinlefts,        ArrayList<sqlview_Relation> sqlview_relations    ) {
        this.sqlview_joinrights = sqlview_joinrights;
        this.sqlview_joinlefts = sqlview_joinlefts;
        this.sqlview_relations = sqlview_relations;
    }


    public List<sqlview_JoinRight> getSqlview_joinrights() {
        return sqlview_joinrights;
    }

    public void addSqlview_joinright(Sqlview_joinright sqlview_joinright) {
        this.sqlview_joinrights.add(sqlview_joinright);
    }
    public sqlview_From getSqlview_from() {
        return sqlview_from;
    }

    public void setSqlview_from(sqlview_From sqlview_from) {
        this.sqlview_from = sqlview_from;
    }
    public List<sqlview_JoinLeft> getSqlview_joinlefts() {
        return sqlview_joinlefts;
    }

    public void addSqlview_joinleft(Sqlview_joinleft sqlview_joinleft) {
        this.sqlview_joinlefts.add(sqlview_joinleft);
    }
    public List<sqlview_Relation> getSqlview_relations() {
        return sqlview_relations;
    }

    public void addSqlview_relation(Sqlview_relation sqlview_relation) {
        this.sqlview_relations.add(sqlview_relation);
    }

}