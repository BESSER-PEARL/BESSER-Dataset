





import java.util.List;
import java.util.ArrayList;

public class model_PrimaryObject  {

    private String featureMapAttributeType1;
    private String unsettableAttributeWithDefault;
    private int id;
    private String featureMapReferenceCollection;
    private String name;
    private String featureMapAttributeType2;
    private String featureMapAttributeCollection;
    private String unsettableAttribute;



    public model_PrimaryObject(
        String featureMapAttributeType1,        String unsettableAttributeWithDefault,        int id,        String featureMapReferenceCollection,        String name,        String featureMapAttributeType2,        String featureMapAttributeCollection,        String unsettableAttribute    ) {
        this.featureMapAttributeType1 = featureMapAttributeType1;
        this.unsettableAttributeWithDefault = unsettableAttributeWithDefault;
        this.id = id;
        this.featureMapReferenceCollection = featureMapReferenceCollection;
        this.name = name;
        this.featureMapAttributeType2 = featureMapAttributeType2;
        this.featureMapAttributeCollection = featureMapAttributeCollection;
        this.unsettableAttribute = unsettableAttribute;
    }


    public String getFeaturemapattributetype1() {
        return featureMapAttributeType1;
    }

    public void setFeaturemapattributetype1(String featureMapAttributeType1) {
        this.featureMapAttributeType1 = featureMapAttributeType1;
    }
    public String getUnsettableattributewithdefault() {
        return unsettableAttributeWithDefault;
    }

    public void setUnsettableattributewithdefault(String unsettableAttributeWithDefault) {
        this.unsettableAttributeWithDefault = unsettableAttributeWithDefault;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getFeaturemapreferencecollection() {
        return featureMapReferenceCollection;
    }

    public void setFeaturemapreferencecollection(String featureMapReferenceCollection) {
        this.featureMapReferenceCollection = featureMapReferenceCollection;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFeaturemapattributetype2() {
        return featureMapAttributeType2;
    }

    public void setFeaturemapattributetype2(String featureMapAttributeType2) {
        this.featureMapAttributeType2 = featureMapAttributeType2;
    }
    public String getFeaturemapattributecollection() {
        return featureMapAttributeCollection;
    }

    public void setFeaturemapattributecollection(String featureMapAttributeCollection) {
        this.featureMapAttributeCollection = featureMapAttributeCollection;
    }
    public String getUnsettableattribute() {
        return unsettableAttribute;
    }

    public void setUnsettableattribute(String unsettableAttribute) {
        this.unsettableAttribute = unsettableAttribute;
    }


}