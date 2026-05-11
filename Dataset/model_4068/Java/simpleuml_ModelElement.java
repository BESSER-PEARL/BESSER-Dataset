





import java.util.List;
import java.util.ArrayList;

public class simpleuml_ModelElement  {

    private String stereotype;
    private String name;



    public simpleuml_ModelElement(
        String stereotype,        String name    ) {
        this.stereotype = stereotype;
        this.name = name;
    }


    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}