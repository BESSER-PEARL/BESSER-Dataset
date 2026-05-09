





import java.util.List;
import java.util.ArrayList;

public class foundation_core_ElementResidence  {

    private String visibility;





    private Component component;




    private ModelElement modelelement;


    public foundation_core_ElementResidence(
        String visibility    ) {
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public Component getComponent() {
        return component;
    }

    public void setComponent(Component component) {
        this.component = component;
    }
    public ModelElement getModelelement() {
        return modelelement;
    }

    public void setModelelement(ModelElement modelelement) {
        this.modelelement = modelelement;
    }

}