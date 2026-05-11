





import java.util.List;
import java.util.ArrayList;

public class CD_Attribute extends NamedElt {

    private String multiValued;





    private CD_Classifier cd_classifier;


    public CD_Attribute(
        String multiValued    ) {
        super(
        );
        this.multiValued = multiValued;
    }


    public String getMultivalued() {
        return multiValued;
    }

    public void setMultivalued(String multiValued) {
        this.multiValued = multiValued;
    }

    public CD_Classifier getCd_classifier() {
        return cd_classifier;
    }

    public void setCd_classifier(CD_Classifier cd_classifier) {
        this.cd_classifier = cd_classifier;
    }

}