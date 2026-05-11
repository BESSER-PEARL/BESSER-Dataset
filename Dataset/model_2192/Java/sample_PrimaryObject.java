





import java.util.List;
import java.util.ArrayList;

public class sample_PrimaryObject  {

    private String id;
    private String featureMapAttributeType2;
    private String featureMapReferenceCollection;
    private String kind;
    private String unsettableAttributeWithDefault;
    private String name;
    private String featureMapAttributeType1;
    private String featureMapAttributeCollection;
    private String unsettableAttribute;



    public sample_PrimaryObject(
        String id,        String featureMapAttributeType2,        String featureMapReferenceCollection,        String kind,        String unsettableAttributeWithDefault,        String name,        String featureMapAttributeType1,        String featureMapAttributeCollection,        String unsettableAttribute    ) {
        this.id = id;
        this.featureMapAttributeType2 = featureMapAttributeType2;
        this.featureMapReferenceCollection = featureMapReferenceCollection;
        this.kind = kind;
        this.unsettableAttributeWithDefault = unsettableAttributeWithDefault;
        this.name = name;
        this.featureMapAttributeType1 = featureMapAttributeType1;
        this.featureMapAttributeCollection = featureMapAttributeCollection;
        this.unsettableAttribute = unsettableAttribute;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFeaturemapattributetype2() {
        return featureMapAttributeType2;
    }

    public void setFeaturemapattributetype2(String featureMapAttributeType2) {
        this.featureMapAttributeType2 = featureMapAttributeType2;
    }
    public String getFeaturemapreferencecollection() {
        return featureMapReferenceCollection;
    }

    public void setFeaturemapreferencecollection(String featureMapReferenceCollection) {
        this.featureMapReferenceCollection = featureMapReferenceCollection;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getUnsettableattributewithdefault() {
        return unsettableAttributeWithDefault;
    }

    public void setUnsettableattributewithdefault(String unsettableAttributeWithDefault) {
        this.unsettableAttributeWithDefault = unsettableAttributeWithDefault;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getUnsettableattribute() {
        return unsettableAttribute;
    }

    public void setUnsettableattribute(String unsettableAttribute) {
        this.unsettableAttribute = unsettableAttribute;
    }


}