





import java.util.List;
import java.util.ArrayList;

public class yuml_Class extends ColorableElement {

    private String stereotype;
    private String name;



    public yuml_Class(
        String stereotype,        String name    ) {
        super(
        );
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