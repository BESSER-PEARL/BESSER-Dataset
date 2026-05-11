





import java.util.List;
import java.util.ArrayList;

public class dbmddandroid_DBScheme extends NamedElement {






    private List<dbmddandroid_Relation> dbmddandroid_relations;


    public dbmddandroid_DBScheme(
    ) {
        super(
        );
        this.dbmddandroid_relations = new ArrayList<>();
    }

    public dbmddandroid_DBScheme(
        ArrayList<dbmddandroid_Relation> dbmddandroid_relations    ) {
        this.dbmddandroid_relations = dbmddandroid_relations;
    }


    public List<dbmddandroid_Relation> getDbmddandroid_relations() {
        return dbmddandroid_relations;
    }

    public void addDbmddandroid_relation(Dbmddandroid_relation dbmddandroid_relation) {
        this.dbmddandroid_relations.add(dbmddandroid_relation);
    }

}