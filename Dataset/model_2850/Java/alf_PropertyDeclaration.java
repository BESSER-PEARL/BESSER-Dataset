





import java.util.List;
import java.util.ArrayList;

public class alf_PropertyDeclaration  {

    private boolean isComposite;





    private alf_Name alf_name;




    private alf_PropertyDefinition alf_propertydefinition;


    public alf_PropertyDeclaration(
        boolean isComposite    ) {
        this.isComposite = isComposite;
    }


    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }

    public alf_Name getAlf_name() {
        return alf_name;
    }

    public void setAlf_name(alf_Name alf_name) {
        this.alf_name = alf_name;
    }
    public alf_PropertyDefinition getAlf_propertydefinition() {
        return alf_propertydefinition;
    }

    public void setAlf_propertydefinition(alf_PropertyDefinition alf_propertydefinition) {
        this.alf_propertydefinition = alf_propertydefinition;
    }

}