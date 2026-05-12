





import java.util.List;
import java.util.ArrayList;

public class Core_Generalization extends Relationship {

    private String discriminator;





    private GeneralizableElement generalizableelement;




    private Classifier classifier;




    private GeneralizableElement generalizableelement;


    public Core_Generalization(
        String discriminator    ) {
        super(
        );
        this.discriminator = discriminator;
    }


    public String getDiscriminator() {
        return discriminator;
    }

    public void setDiscriminator(String discriminator) {
        this.discriminator = discriminator;
    }

    public GeneralizableElement getGeneralizableelement() {
        return generalizableelement;
    }

    public void setGeneralizableelement(GeneralizableElement generalizableelement) {
        this.generalizableelement = generalizableelement;
    }
    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }
    public GeneralizableElement getGeneralizableelement() {
        return generalizableelement;
    }

    public void setGeneralizableelement(GeneralizableElement generalizableelement) {
        this.generalizableelement = generalizableelement;
    }

}