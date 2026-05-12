





import java.util.List;
import java.util.ArrayList;

public class Core_ModelElement extends Element {

    private String visibility;
    private String isSpecification;
    private String name;



    public Core_ModelElement(
        String visibility,        String isSpecification,        String name    ) {
        super(
        );
        this.visibility = visibility;
        this.isSpecification = isSpecification;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getIsspecification() {
        return isSpecification;
    }

    public void setIsspecification(String isSpecification) {
        this.isSpecification = isSpecification;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}