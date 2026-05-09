





import java.util.List;
import java.util.ArrayList;

public class model_PrimaryObject  {

    private String featureMapAttributeType2;
    private String featureMapAttributeType1;
    private String featureMapAttributeCollection;
    private String name;
    private String featureMapReferenceCollection;



    public model_PrimaryObject(
        String featureMapAttributeType2,        String featureMapAttributeType1,        String featureMapAttributeCollection,        String name,        String featureMapReferenceCollection    ) {
        this.featureMapAttributeType2 = featureMapAttributeType2;
        this.featureMapAttributeType1 = featureMapAttributeType1;
        this.featureMapAttributeCollection = featureMapAttributeCollection;
        this.name = name;
        this.featureMapReferenceCollection = featureMapReferenceCollection;
    }


    public String getFeaturemapattributetype2() {
        return featureMapAttributeType2;
    }

    public void setFeaturemapattributetype2(String featureMapAttributeType2) {
        this.featureMapAttributeType2 = featureMapAttributeType2;
    }
    public String getFeaturemapattributetype1() {
        return featureMapAttributeType1;
    }

    public void setFeaturemapattributetype1(String featureMapAttributeType1) {
        this.featureMapAttributeType1 = featureMapAttributeType1;
    }
    public String getFeaturemapattributecollection() {
        return featureMapAttributeCollection;
    }

    public void setFeaturemapattributecollection(String featureMapAttributeCollection) {
        this.featureMapAttributeCollection = featureMapAttributeCollection;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFeaturemapreferencecollection() {
        return featureMapReferenceCollection;
    }

    public void setFeaturemapreferencecollection(String featureMapReferenceCollection) {
        this.featureMapReferenceCollection = featureMapReferenceCollection;
    }


}