





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_ResolutionModel  {

    private String name;





    private List<cvlmodel_VSpecResolution> cvlmodel_vspecresolutions;




    private cvlmodel_VSpecTree cvlmodel_vspectree;


    public cvlmodel_ResolutionModel(
        String name    ) {
        this.name = name;
        this.cvlmodel_vspecresolutions = new ArrayList<>();
    }

    public cvlmodel_ResolutionModel(
        String name        ArrayList<cvlmodel_VSpecResolution> cvlmodel_vspecresolutions    ) {
        this.name = name;
        this.cvlmodel_vspecresolutions = cvlmodel_vspecresolutions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<cvlmodel_VSpecResolution> getCvlmodel_vspecresolutions() {
        return cvlmodel_vspecresolutions;
    }

    public void addCvlmodel_vspecresolution(Cvlmodel_vspecresolution cvlmodel_vspecresolution) {
        this.cvlmodel_vspecresolutions.add(cvlmodel_vspecresolution);
    }
    public cvlmodel_VSpecTree getCvlmodel_vspectree() {
        return cvlmodel_vspectree;
    }

    public void setCvlmodel_vspectree(cvlmodel_VSpecTree cvlmodel_vspectree) {
        this.cvlmodel_vspectree = cvlmodel_vspectree;
    }

}