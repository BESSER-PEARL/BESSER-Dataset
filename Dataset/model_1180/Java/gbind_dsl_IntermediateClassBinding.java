





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_IntermediateClassBinding extends ConceptBinding {

    private String conceptReferenceName;



    public gbind_dsl_IntermediateClassBinding(
        String conceptReferenceName    ) {
        super(
        );
        this.conceptReferenceName = conceptReferenceName;
    }


    public String getConceptreferencename() {
        return conceptReferenceName;
    }

    public void setConceptreferencename(String conceptReferenceName) {
        this.conceptReferenceName = conceptReferenceName;
    }


}