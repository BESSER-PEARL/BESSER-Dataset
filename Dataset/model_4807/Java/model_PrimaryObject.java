





import java.util.List;
import java.util.ArrayList;

public class model_PrimaryObject  {

    private String featureMapAttributeType1;
    private String featureMapAttributeType2;
    private String unsettableAttribute;
    private String unsettableAttributeWithNonNullDefault;
    private String featureMapReferenceCollection;
    private String name;
    private String featureMapAttributeCollection;
    private String idAttribute;





    private model_PrimaryObject model_primaryobject;


    public model_PrimaryObject(
        String featureMapAttributeType1,        String featureMapAttributeType2,        String unsettableAttribute,        String unsettableAttributeWithNonNullDefault,        String featureMapReferenceCollection,        String name,        String featureMapAttributeCollection,        String idAttribute    ) {
        this.featureMapAttributeType1 = featureMapAttributeType1;
        this.featureMapAttributeType2 = featureMapAttributeType2;
        this.unsettableAttribute = unsettableAttribute;
        this.unsettableAttributeWithNonNullDefault = unsettableAttributeWithNonNullDefault;
        this.featureMapReferenceCollection = featureMapReferenceCollection;
        this.name = name;
        this.featureMapAttributeCollection = featureMapAttributeCollection;
        this.idAttribute = idAttribute;
    }


    public String getFeaturemapattributetype1() {
        return featureMapAttributeType1;
    }

    public void setFeaturemapattributetype1(String featureMapAttributeType1) {
        this.featureMapAttributeType1 = featureMapAttributeType1;
    }
    public String getFeaturemapattributetype2() {
        return featureMapAttributeType2;
    }

    public void setFeaturemapattributetype2(String featureMapAttributeType2) {
        this.featureMapAttributeType2 = featureMapAttributeType2;
    }
    public String getUnsettableattribute() {
        return unsettableAttribute;
    }

    public void setUnsettableattribute(String unsettableAttribute) {
        this.unsettableAttribute = unsettableAttribute;
    }
    public String getUnsettableattributewithnonnulldefault() {
        return unsettableAttributeWithNonNullDefault;
    }

    public void setUnsettableattributewithnonnulldefault(String unsettableAttributeWithNonNullDefault) {
        this.unsettableAttributeWithNonNullDefault = unsettableAttributeWithNonNullDefault;
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
    public String getIdattribute() {
        return idAttribute;
    }

    public void setIdattribute(String idAttribute) {
        this.idAttribute = idAttribute;
    }

    public model_PrimaryObject getModel_primaryobject() {
        return model_primaryobject;
    }

    public void setModel_primaryobject(model_PrimaryObject model_primaryobject) {
        this.model_primaryobject = model_primaryobject;
    }

}