





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Method  {

    private String name;
    private String body;





    private domainmodel_Entity domainmodel_entity;


    public domainmodel_Method(
        String name,        String body    ) {
        this.name = name;
        this.body = body;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public domainmodel_Entity getDomainmodel_entity() {
        return domainmodel_entity;
    }

    public void setDomainmodel_entity(domainmodel_Entity domainmodel_entity) {
        this.domainmodel_entity = domainmodel_entity;
    }

}