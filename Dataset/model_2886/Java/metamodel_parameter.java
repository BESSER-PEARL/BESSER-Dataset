





import java.util.List;
import java.util.ArrayList;

public class metamodel_parameter  {

    private String name;





    private metamodel_Query metamodel_query;


    public metamodel_parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodel_Query getMetamodel_query() {
        return metamodel_query;
    }

    public void setMetamodel_query(metamodel_Query metamodel_query) {
        this.metamodel_query = metamodel_query;
    }

}