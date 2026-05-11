





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_Multiplicity  {

    private String max;
    private String min;





    private List<cvlmodel_VSpec> cvlmodel_vspecs;




    private cvlmodel_VSpec cvlmodel_vspec;


    public cvlmodel_Multiplicity(
        String max,        String min    ) {
        this.max = max;
        this.min = min;
        this.cvlmodel_vspecs = new ArrayList<>();
    }

    public cvlmodel_Multiplicity(
        String max,        String min        ArrayList<cvlmodel_VSpec> cvlmodel_vspecs    ) {
        this.max = max;
        this.min = min;
        this.cvlmodel_vspecs = cvlmodel_vspecs;
    }

    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
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