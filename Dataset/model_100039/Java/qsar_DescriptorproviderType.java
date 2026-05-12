





import java.util.List;
import java.util.ArrayList;

public class qsar_DescriptorproviderType  {

    private String id;
    private String name;
    private String vendor;
    private String uRL;
    private String version;



    public qsar_DescriptorproviderType(
        String id,        String name,        String vendor,        String uRL,        String version    ) {
        this.id = id;
        this.name = name;
        this.vendor = vendor;
        this.uRL = uRL;
        this.version = version;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}