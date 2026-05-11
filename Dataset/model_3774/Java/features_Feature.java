





import java.util.List;
import java.util.ArrayList;

public class features_Feature extends FeatureDescriptor {

    private String identifier;
    private String description;
    private String provider;
    private String name;



    public features_Feature(
        String identifier,        String description,        String provider,        String name    ) {
        super(
        );
        this.identifier = identifier;
        this.description = description;
        this.provider = provider;
        this.name = name;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}