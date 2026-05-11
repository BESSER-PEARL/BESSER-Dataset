





import java.util.List;
import java.util.ArrayList;

public class model_business_BusinessView extends BusinessColumnSet {






    private List<BusinessViewInnerJoinRelationship> businessviewinnerjoinrelationships;


    public model_business_BusinessView(
    ) {
        super(
        );
        this.businessviewinnerjoinrelationships = new ArrayList<>();
    }

    public model_business_BusinessView(
        ArrayList<BusinessViewInnerJoinRelationship> businessviewinnerjoinrelationships    ) {
        this.businessviewinnerjoinrelationships = businessviewinnerjoinrelationships;
    }


    public List<BusinessViewInnerJoinRelationship> getBusinessviewinnerjoinrelationships() {
        return businessviewinnerjoinrelationships;
    }

    public void addBusinessviewinnerjoinrelationship(Businessviewinnerjoinrelationship businessviewinnerjoinrelationship) {
        this.businessviewinnerjoinrelationships.add(businessviewinnerjoinrelationship);
    }

}