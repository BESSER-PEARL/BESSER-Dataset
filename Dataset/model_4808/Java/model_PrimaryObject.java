





import java.util.List;
import java.util.ArrayList;

public class model_PrimaryObject  {

    private String unsettableAttribute;
    private String featureMapAttributeType2;
    private String featureMapAttributeCollection;
    private String idAttribute;
    private String name;
    private String unsettableAttributeWithNonNullDefault;
    private String featureMapReferenceCollection;
    private String featureMapAttributeType1;





    private model_PrimaryObject model_primaryobject;


    public model_PrimaryObject(
        String unsettableAttribute,        String featureMapAttributeType2,        String featureMapAttributeCollection,        String idAttribute,        String name,        String unsettableAttributeWithNonNullDefault,        String featureMapReferenceCollection,        String featureMapAttributeType1    ) {
        this.unsettableAttribute = unsettableAttribute;
        this.featureMapAttributeType2 = featureMapAttributeType2;
        this.featureMapAttributeCollection = featureMapAttributeCollection;
        this.idAttribute = idAttribute;
        this.name = name;
        this.unsettableAttributeWithNonNullDefault = unsettableAttributeWithNonNullDefault;
        this.featureMapReferenceCollection = featureMapReferenceCollection;
        this.featureMapAttributeType1 = featureMapAttributeType1;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getFeaturemapattributetype1() {
        return featureMapAttributeType1;
    }

    public void setFeaturemapattributetype1(String featureMapAttributeType1) {
        this.featureMapAttributeType1 = featureMapAttributeType1;
    }

    public model_PrimaryObject getModel_primaryobject() {
        return model_primaryobject;
    }

    public void setModel_primaryobject(model_PrimaryObject model_primaryobject) {
        this.model_primaryobject = model_primaryobject;
    }

}