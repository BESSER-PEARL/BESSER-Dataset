





import java.util.List;
import java.util.ArrayList;

public class UsecaseDSL_UseCaseDiagram_c extends Classifier {






    private List<UsecaseDSL_Relationship> usecasedsl_relationships;


    public UsecaseDSL_UseCaseDiagram_c(
    ) {
        super(
        );
        this.usecasedsl_relationships = new ArrayList<>();
    }

    public UsecaseDSL_UseCaseDiagram_c(
        ArrayList<UsecaseDSL_Relationship> usecasedsl_relationships    ) {
        this.usecasedsl_relationships = usecasedsl_relationships;
    }


    public List<UsecaseDSL_Relationship> getUsecasedsl_relationships() {
        return usecasedsl_relationships;
    }

    public void addUsecasedsl_relationship(Usecasedsl_relationship usecasedsl_relationship) {
        this.usecasedsl_relationships.add(usecasedsl_relationship);
    }

}