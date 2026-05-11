





import java.util.List;
import java.util.ArrayList;

public class aadl2_Classifier extends Type, Namespace {

    private String noPrototypes;
    private String noProperties;
    private String noAnnexes;





    private aadl2_Classifier aadl2_classifier;




    private aadl2_Property aadl2_property;


    public aadl2_Classifier(
        String noPrototypes,        String noProperties,        String noAnnexes    ) {
        super(
        );
        this.noPrototypes = noPrototypes;
        this.noProperties = noProperties;
        this.noAnnexes = noAnnexes;
    }


    public String getNoprototypes() {
        return noPrototypes;
    }

    public void setNoprototypes(String noPrototypes) {
        this.noPrototypes = noPrototypes;
    }
    public String getNoproperties() {
        return noProperties;
    }

    public void setNoproperties(String noProperties) {
        this.noProperties = noProperties;
    }
    public String getNoannexes() {
        return noAnnexes;
    }

    public void setNoannexes(String noAnnexes) {
        this.noAnnexes = noAnnexes;
    }

    public aadl2_Classifier getAadl2_classifier() {
        return aadl2_classifier;
    }

    public void setAadl2_classifier(aadl2_Classifier aadl2_classifier) {
        this.aadl2_classifier = aadl2_classifier;
    }
    public aadl2_Property getAadl2_property() {
        return aadl2_property;
    }

    public void setAadl2_property(aadl2_Property aadl2_property) {
        this.aadl2_property = aadl2_property;
    }

}