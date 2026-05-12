





import java.util.List;
import java.util.ArrayList;

public class qsar_PreprocessingStepType  {

    private String namespace;
    private String id;
    private String vendor;
    private String name;
    private String order;



    public qsar_PreprocessingStepType(
        String namespace,        String id,        String vendor,        String name,        String order    ) {
        this.namespace = namespace;
        this.id = id;
        this.vendor = vendor;
        this.name = name;
        this.order = order;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }


}