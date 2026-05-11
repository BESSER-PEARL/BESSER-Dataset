





import java.util.List;
import java.util.ArrayList;

public class smalluml_Package  {






    private List<smalluml_Class> smalluml_classs;




    private List<smalluml_Relation> smalluml_relations;


    public smalluml_Package(
    ) {
        this.smalluml_classs = new ArrayList<>();
        this.smalluml_relations = new ArrayList<>();
    }

    public smalluml_Package(
        ArrayList<smalluml_Class> smalluml_classs,        ArrayList<smalluml_Relation> smalluml_relations    ) {
        this.smalluml_classs = smalluml_classs;
        this.smalluml_relations = smalluml_relations;
    }


    public List<smalluml_Class> getSmalluml_classs() {
        return smalluml_classs;
    }

    public void addSmalluml_class(Smalluml_class smalluml_class) {
        this.smalluml_classs.add(smalluml_class);
    }
    public List<smalluml_Relation> getSmalluml_relations() {
        return smalluml_relations;
    }

    public void addSmalluml_relation(Smalluml_relation smalluml_relation) {
        this.smalluml_relations.add(smalluml_relation);
    }

}