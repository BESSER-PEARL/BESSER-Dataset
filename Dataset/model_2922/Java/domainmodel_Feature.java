





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Feature  {

    private String name;
    private String not_;
    private String key;





    private domainmodel_Type domainmodel_type;




    private domainmodel_Entity domainmodel_entity;


    public domainmodel_Feature(
        String name,        String not_,        String key    ) {
        this.name = name;
        this.not_ = not_;
        this.key = key;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNot_() {
        return not_;
    }

    public void setNot_(String not_) {
        this.not_ = not_;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public domainmodel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainmodel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }
    public domainmodel_Entity getDomainmodel_entity() {
        return domainmodel_entity;
    }

    public void setDomainmodel_entity(domainmodel_Entity domainmodel_entity) {
        this.domainmodel_entity = domainmodel_entity;
    }

}