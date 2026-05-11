





import java.util.List;
import java.util.ArrayList;

public class camel_location_GeographicalRegion extends Location {

    private String alternativeNames;
    private String name;



    public camel_location_GeographicalRegion(
        String alternativeNames,        String name    ) {
        super(
        );
        this.alternativeNames = alternativeNames;
        this.name = name;
    }


    public String getAlternativenames() {
        return alternativeNames;
    }

    public void setAlternativenames(String alternativeNames) {
        this.alternativeNames = alternativeNames;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}