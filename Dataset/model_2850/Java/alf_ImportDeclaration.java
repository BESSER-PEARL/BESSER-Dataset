





import java.util.List;
import java.util.ArrayList;

public class alf_ImportDeclaration  {

    private String visibility;





    private alf_ImportReference alf_importreference;




    private alf_UnitDefinition alf_unitdefinition;


    public alf_ImportDeclaration(
        String visibility    ) {
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public alf_ImportReference getAlf_importreference() {
        return alf_importreference;
    }

    public void setAlf_importreference(alf_ImportReference alf_importreference) {
        this.alf_importreference = alf_importreference;
    }
    public alf_UnitDefinition getAlf_unitdefinition() {
        return alf_unitdefinition;
    }

    public void setAlf_unitdefinition(alf_UnitDefinition alf_unitdefinition) {
        this.alf_unitdefinition = alf_unitdefinition;
    }

}