





import java.util.List;
import java.util.ArrayList;

public class build_Repository  {

    private String location;
    private String label;





    private build_Contribution build_contribution;


    public build_Repository(
        String location,        String label    ) {
        this.location = location;
        this.label = label;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public build_Contribution getBuild_contribution() {
        return build_contribution;
    }

    public void setBuild_contribution(build_Contribution build_contribution) {
        this.build_contribution = build_contribution;
    }

}