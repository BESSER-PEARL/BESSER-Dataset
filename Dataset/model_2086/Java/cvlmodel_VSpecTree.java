





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_VSpecTree  {






    private List<cvlmodel_VSpec> cvlmodel_vspecs;




    private cvlmodel_VSpec cvlmodel_vspec;


    public cvlmodel_VSpecTree(
    ) {
        this.cvlmodel_vspecs = new ArrayList<>();
    }

    public cvlmodel_VSpecTree(
        ArrayList<cvlmodel_VSpec> cvlmodel_vspecs    ) {
        this.cvlmodel_vspecs = cvlmodel_vspecs;
    }


    public List<cvlmodel_VSpec> getCvlmodel_vspecs() {
        return cvlmodel_vspecs;
    }

    public void addCvlmodel_vspec(Cvlmodel_vspec cvlmodel_vspec) {
        this.cvlmodel_vspecs.add(cvlmodel_vspec);
    }
    public cvlmodel_VSpec getCvlmodel_vspec() {
        return cvlmodel_vspec;
    }

    public void setCvlmodel_vspec(cvlmodel_VSpec cvlmodel_vspec) {
        this.cvlmodel_vspec = cvlmodel_vspec;
    }

}