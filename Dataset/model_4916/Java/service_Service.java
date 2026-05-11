





import java.util.List;
import java.util.ArrayList;

public class service_Service  {

    private String namespace;
    private String description;
    private String name;



    public service_Service(
        String namespace,        String description,        String name    ) {
        this.namespace = namespace;
        this.description = description;
        this.name = name;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}