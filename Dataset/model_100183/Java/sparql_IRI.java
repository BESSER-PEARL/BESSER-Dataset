





import java.util.List;
import java.util.ArrayList;

public class sparql_IRI extends GraphNode {

    private String value;





    private sparql_Base sparql_base;


    public sparql_IRI(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public sparql_Base getSparql_base() {
        return sparql_base;
    }

    public void setSparql_base(sparql_Base sparql_base) {
        this.sparql_base = sparql_base;
    }

}