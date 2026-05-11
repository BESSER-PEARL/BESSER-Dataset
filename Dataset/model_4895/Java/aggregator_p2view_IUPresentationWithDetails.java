





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_IUPresentationWithDetails extends p2view_IUPresentation, p2view_IUDetails {

    private String detailsResolved;



    public aggregator_p2view_IUPresentationWithDetails(
        String detailsResolved    ) {
        super(
        );
        this.detailsResolved = detailsResolved;
    }


    public String getDetailsresolved() {
        return detailsResolved;
    }

    public void setDetailsresolved(String detailsResolved) {
        this.detailsResolved = detailsResolved;
    }


}