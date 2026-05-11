





import java.util.List;
import java.util.ArrayList;

public class smalluml_Package extends NamedElement {






    private List<smalluml_Relation> smalluml_relations;




    private List<smalluml_Class> smalluml_classs;


    public smalluml_Package(
    ) {
        super(
        );
        this.smalluml_relations = new ArrayList<>();
        this.smalluml_classs = new ArrayList<>();
    }

    public smalluml_Package(
        ArrayList<smalluml_Relation> smalluml_relations,        ArrayList<smalluml_Class> smalluml_classs    ) {
        this.smalluml_relations = smalluml_relations;
        this.smalluml_classs = smalluml_classs;
    }


    public List<smalluml_Relation> getSmalluml_relations() {
        return smalluml_relations;
    }

    public void addSmalluml_relation(Smalluml_relation smalluml_relation) {
        this.smalluml_relations.add(smalluml_relation);
    }
    public List<smalluml_Class> getSmalluml_classs() {
        return smalluml_classs;
    }

    public void addSmalluml_class(Smalluml_class smalluml_class) {
        this.smalluml_classs.add(smalluml_class);
    }

}