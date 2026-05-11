





import java.util.List;
import java.util.ArrayList;

public class metamodel_Entity extends Type {






    private List<metamodel_Query> metamodel_querys;




    private metamodel_Query metamodel_query;


    public metamodel_Entity(
    ) {
        super(
        );
        this.metamodel_querys = new ArrayList<>();
    }

    public metamodel_Entity(
        ArrayList<metamodel_Query> metamodel_querys    ) {
        this.metamodel_querys = metamodel_querys;
    }


    public List<metamodel_Query> getMetamodel_querys() {
        return metamodel_querys;
    }

    public void addMetamodel_query(Metamodel_query metamodel_query) {
        this.metamodel_querys.add(metamodel_query);
    }
    public metamodel_Query getMetamodel_query() {
        return metamodel_query;
    }

    public void setMetamodel_query(metamodel_Query metamodel_query) {
        this.metamodel_query = metamodel_query;
    }

}