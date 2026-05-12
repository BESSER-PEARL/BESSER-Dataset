





import java.util.List;
import java.util.ArrayList;

public class Core_Generalization_ extends Relationship {

    private String discriminator;





    private Classifier classifier;


    public Core_Generalization_(
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