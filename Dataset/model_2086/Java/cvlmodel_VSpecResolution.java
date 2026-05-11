





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_VSpecResolution  {

    private String name;





    private cvlmodel_VSpec cvlmodel_vspec;


    public cvlmodel_VSpecResolution(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cvlmodel_VSpec getCvlmodel_vspec() {
        return cvlmodel_vspec;
    }

    public void setCvlmodel_vspec(cvlmodel_VSpec cvlmodel_vspec) {
        this.cvlmodel_vspec = cvlmodel_vspec;
    }

}