





import java.util.List;
import java.util.ArrayList;

public class aredsl_CreateInstanceOperation extends DomainOperation {

    private String name;
    private String feature;
    private String type;



    public aredsl_CreateInstanceOperation(
        String name,        String feature,        String type    ) {
        super(
        );
        this.name = name;
        this.feature = feature;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}