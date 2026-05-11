





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_CVLModel  {

    private String name;





    private cvlmodel_VSpecTree cvlmodel_vspectree;




    private List<cvlmodel_VariationPoint> cvlmodel_variationpoints;


    public cvlmodel_CVLModel(
        String name    ) {
        this.name = name;
        this.cvlmodel_variationpoints = new ArrayList<>();
    }

    public cvlmodel_CVLModel(
        String name        ArrayList<cvlmodel_VariationPoint> cvlmodel_variationpoints    ) {
        this.name = name;
        this.cvlmodel_variationpoints = cvlmodel_variationpoints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cvlmodel_VSpecTree getCvlmodel_vspectree() {
        return cvlmodel_vspectree;
    }

    public void setCvlmodel_vspectree(cvlmodel_VSpecTree cvlmodel_vspectree) {
        this.cvlmodel_vspectree = cvlmodel_vspectree;
    }
    public List<cvlmodel_VariationPoint> getCvlmodel_variationpoints() {
        return cvlmodel_variationpoints;
    }

    public void addCvlmodel_variationpoint(Cvlmodel_variationpoint cvlmodel_variationpoint) {
        this.cvlmodel_variationpoints.add(cvlmodel_variationpoint);
    }

}