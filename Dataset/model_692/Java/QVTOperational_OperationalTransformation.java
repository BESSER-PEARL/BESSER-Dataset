





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_OperationalTransformation extends Module {






    private List<Property> propertys;




    private List<Class> classs;




    private List<Relation> relations;




    private RelationalTransformation relationaltransformation;


    public QVTOperational_OperationalTransformation(
    ) {
        super(
        );
        this.propertys = new ArrayList<>();
        this.classs = new ArrayList<>();
        this.relations = new ArrayList<>();
    }

    public QVTOperational_OperationalTransformation(
        ArrayList<Property> propertys,        ArrayList<Class> classs,        ArrayList<Relation> relations    ) {
        this.propertys = propertys;
        this.classs = classs;
        this.relations = relations;
    }


    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
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
    public RelationalTransformation getRelationaltransformation() {
        return relationaltransformation;
    }

    public void setRelationaltransformation(RelationalTransformation relationaltransformation) {
        this.relationaltransformation = relationaltransformation;
    }

}