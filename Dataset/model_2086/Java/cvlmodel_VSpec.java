





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_VSpec  {

    private String name;
    private String mandatory;





    private cvlmodel_VSpec cvlmodel_vspec;




    private List<cvlmodel_VSpec> cvlmodel_vspecs;


    public cvlmodel_VSpec(
        String name,        String mandatory    ) {
        this.name = name;
        this.mandatory = mandatory;
        this.cvlmodel_vspecs = new ArrayList<>();
    }

    public cvlmodel_VSpec(
        String name,        String mandatory        ArrayList<cvlmodel_VSpec> cvlmodel_vspecs    ) {
        this.name = name;
        this.mandatory = mandatory;
        this.cvlmodel_vspecs = cvlmodel_vspecs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMandatory() {
        return mandatory;
    }

    public void setMandatory(String mandatory) {
        this.mandatory = mandatory;
    }

    public cvlmodel_VSpec getCvlmodel_vspec() {
        return cvlmodel_vspec;
    }

    public void setCvlmodel_vspec(cvlmodel_VSpec cvlmodel_vspec) {
        this.cvlmodel_vspec = cvlmodel_vspec;
    }
    public List<cvlmodel_VSpec> getCvlmodel_vspecs() {
        return cvlmodel_vspecs;
    }

    public void addCvlmodel_vspec(Cvlmodel_vspec cvlmodel_vspec) {
        this.cvlmodel_vspecs.add(cvlmodel_vspec);
    }

}