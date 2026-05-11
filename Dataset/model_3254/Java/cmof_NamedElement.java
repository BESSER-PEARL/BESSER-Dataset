





import java.util.List;
import java.util.ArrayList;

public class cmof_NamedElement extends Element {

    private String visibility;
    private String name;





    private cmof_Classifier cmof_classifier;


    public cmof_NamedElement(
        String visibility,        String name    ) {
        super(
        );
        this.visibility = visibility;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cmof_Classifier getCmof_classifier() {
        return cmof_classifier;
    }

    public void setCmof_classifier(cmof_Classifier cmof_classifier) {
        this.cmof_classifier = cmof_classifier;
    }

}