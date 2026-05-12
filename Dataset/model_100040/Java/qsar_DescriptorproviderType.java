





import java.util.List;
import java.util.ArrayList;

public class qsar_DescriptorproviderType  {

    private String uRL;
    private String name;
    private String version;
    private String vendor;
    private String id;



    public qsar_DescriptorproviderType(
        String uRL,        String name,        String version,        String vendor,        String id    ) {
        this.uRL = uRL;
        this.name = name;
        this.version = version;
        this.vendor = vendor;
        this.id = id;
    }


    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}