





import java.util.List;
import java.util.ArrayList;

public class foundation_core_Generalization extends Relationship {

    private String discriminator;





    private Classifier classifier;


    public foundation_core_Generalization(
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

    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }

}