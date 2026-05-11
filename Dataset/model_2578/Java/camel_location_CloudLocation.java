





import java.util.List;
import java.util.ArrayList;

public class camel_location_CloudLocation extends Location {

    private boolean isAssignable;





    private CloudLocation cloudlocation;




    private List<CloudLocation> cloudlocations;




    private GeographicalRegion geographicalregion;


    public camel_location_CloudLocation(
        boolean isAssignable    ) {
        super(
        );
        this.isAssignable = isAssignable;
        this.cloudlocations = new ArrayList<>();
    }

    public camel_location_CloudLocation(
        boolean isAssignable        ArrayList<CloudLocation> cloudlocations    ) {
        this.isAssignable = isAssignable;
        this.cloudlocations = cloudlocations;
    }

    public boolean getIsassignable() {
        return isAssignable;
    }

    public void setIsassignable(boolean isAssignable) {
        this.isAssignable = isAssignable;
    }

    public CloudLocation getCloudlocation() {
        return cloudlocation;
    }

    public void setCloudlocation(CloudLocation cloudlocation) {
        this.cloudlocation = cloudlocation;
    }
    public List<CloudLocation> getCloudlocations() {
        return cloudlocations;
    }

    public void addCloudlocation(Cloudlocation cloudlocation) {
        this.cloudlocations.add(cloudlocation);
    }
    public GeographicalRegion getGeographicalregion() {
        return geographicalregion;
    }

    public void setGeographicalregion(GeographicalRegion geographicalregion) {
        this.geographicalregion = geographicalregion;
    }

}