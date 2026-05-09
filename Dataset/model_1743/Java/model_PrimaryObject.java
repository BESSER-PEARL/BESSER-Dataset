





import java.util.List;
import java.util.ArrayList;

public class model_PrimaryObject  {

    private String featureMapAttributeType1;
    private int id;
    private String unsettableAttribute;
    private String featureMapAttributeType2;
    private String unsettableAttributeWithDefault;
    private String featureMapReferenceCollection;
    private String name;
    private String featureMapAttributeCollection;



    public model_PrimaryObject(
        String featureMapAttributeType1,        int id,        String unsettableAttribute,        String featureMapAttributeType2,        String unsettableAttributeWithDefault,        String featureMapReferenceCollection,        String name,        String featureMapAttributeCollection    ) {
        this.featureMapAttributeType1 = featureMapAttributeType1;
        this.id = id;
        this.unsettableAttribute = unsettableAttribute;
        this.featureMapAttributeType2 = featureMapAttributeType2;
        this.unsettableAttributeWithDefault = unsettableAttributeWithDefault;
        this.featureMapReferenceCollection = featureMapReferenceCollection;
        this.name = name;
        this.featureMapAttributeCollection = featureMapAttributeCollection;
    }


    public String getFeaturemapattributetype1() {
        return featureMapAttributeType1;
    }

    public void setFeaturemapattributetype1(String featureMapAttributeType1) {
        this.featureMapAttributeType1 = featureMapAttributeType1;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getUnsettableattribute() {
        return unsettableAttribute;
    }

    public void setUnsettableattribute(String unsettableAttribute) {
        this.unsettableAttribute = unsettableAttribute;
    }
    public String getFeaturemapattributetype2() {
        return featureMapAttributeType2;
    }

    public void setFeaturemapattributetype2(String featureMapAttributeType2) {
        this.featureMapAttributeType2 = featureMapAttributeType2;
    }
    public String getUnsettableattributewithdefault() {
        return unsettableAttributeWithDefault;
    }

    public void setUnsettableattributewithdefault(String unsettableAttributeWithDefault) {
        this.unsettableAttributeWithDefault = unsettableAttributeWithDefault;
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
    public String getFeaturemapattributecollection() {
        return featureMapAttributeCollection;
    }

    public void setFeaturemapattributecollection(String featureMapAttributeCollection) {
        this.featureMapAttributeCollection = featureMapAttributeCollection;
    }


}