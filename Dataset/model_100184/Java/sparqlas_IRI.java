





import java.util.List;
import java.util.ArrayList;

public class sparqlas_IRI  {

    private String id;





    private sparqlas_OntologyDocument sparqlas_ontologydocument;


    public sparqlas_IRI(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public sparqlas_OntologyDocument getSparqlas_ontologydocument() {
        return sparqlas_ontologydocument;
    }

    public void setSparqlas_ontologydocument(sparqlas_OntologyDocument sparqlas_ontologydocument) {
        this.sparqlas_ontologydocument = sparqlas_ontologydocument;
    }

}