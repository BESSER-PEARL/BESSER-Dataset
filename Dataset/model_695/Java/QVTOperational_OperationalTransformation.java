





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_OperationalTransformation extends Module {






    private List<Class> classs;




    private List<Relation> relations;




    private List<Property> propertys;




    private RelationalTransformation relationaltransformation;


    public QVTOperational_OperationalTransformation(
    ) {
        super(
        );
        this.classs = new ArrayList<>();
        this.relations = new ArrayList<>();
        this.propertys = new ArrayList<>();
    }

    public QVTOperational_OperationalTransformation(
        ArrayList<Class> classs,        ArrayList<Relation> relations,        ArrayList<Property> propertys    ) {
        this.classs = classs;
        this.relations = relations;
        this.propertys = propertys;
    }


    public List<Class> getClasss() {
        return classs;
    }

    public void addClass(Class class) {
        this.classs.add(class);
    }
    public List<Relation> getRelations() {
        return relations;
    }

    public void addRelation(Relation relation) {
        this.relations.add(relation);
    }
    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }
    public RelationalTransformation getRelationaltransformation() {
        return relationaltransformation;
    }

    public void setRelationaltransformation(RelationalTransformation relationaltransformation) {
        this.relationaltransformation = relationaltransformation;
    }

}