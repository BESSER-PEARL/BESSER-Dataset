





import java.util.List;
import java.util.ArrayList;

public class Tenant  {

    private String tenant_id;





    private List<Property> propertys;


    public Tenant(
        String tenant_id    ) {
        this.tenant_id = tenant_id;
        this.propertys = new ArrayList<>();
    }

    public Tenant(
        String tenant_id        ArrayList<Property> propertys    ) {
        this.tenant_id = tenant_id;
        this.propertys = propertys;
    }

    public String getTenant_id() {
        return tenant_id;
    }

    public void setTenant_id(String tenant_id) {
        this.tenant_id = tenant_id;
    }

    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}