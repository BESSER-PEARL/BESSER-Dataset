





import java.util.List;
import java.util.ArrayList;

public class gastm_AggregateType extends DataType {






    private List<gastm_MemberObject> gastm_memberobjects;




    private gastm_AggregateTypeDefinition gastm_aggregatetypedefinition;




    private gastm_AggregateScope gastm_aggregatescope;


    public gastm_AggregateType(
    ) {
        super(
        );
        this.gastm_memberobjects = new ArrayList<>();
    }

    public gastm_AggregateType(
        ArrayList<gastm_MemberObject> gastm_memberobjects    ) {
        this.gastm_memberobjects = gastm_memberobjects;
    }


    public List<gastm_MemberObject> getGastm_memberobjects() {
        return gastm_memberobjects;
    }

    public void addGastm_memberobject(Gastm_memberobject gastm_memberobject) {
        this.gastm_memberobjects.add(gastm_memberobject);
    }
    public gastm_AggregateTypeDefinition getGastm_aggregatetypedefinition() {
        return gastm_aggregatetypedefinition;
    }

    public void setGastm_aggregatetypedefinition(gastm_AggregateTypeDefinition gastm_aggregatetypedefinition) {
        this.gastm_aggregatetypedefinition = gastm_aggregatetypedefinition;
    }
    public gastm_AggregateScope getGastm_aggregatescope() {
        return gastm_aggregatescope;
    }

    public void setGastm_aggregatescope(gastm_AggregateScope gastm_aggregatescope) {
        this.gastm_aggregatescope = gastm_aggregatescope;
    }

}