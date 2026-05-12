





import java.util.List;
import java.util.ArrayList;

public class qsar_PreprocessingStepType  {

    private String id;
    private String namespace;
    private String vendor;
    private String order;
    private String name;



    public qsar_PreprocessingStepType(
        String id,        String namespace,        String vendor,        String order,        String name    ) {
        this.id = id;
        this.namespace = namespace;
        this.vendor = vendor;
        this.order = order;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}