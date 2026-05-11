





import java.util.List;
import java.util.ArrayList;

public class cloudml_CloudMLElementWithProperties extends CloudMLElement {






    private List<cloudml_PuppetResource> cloudml_puppetresources;




    private List<cloudml_Property> cloudml_propertys;




    private List<cloudml_Resource> cloudml_resources;


    public cloudml_CloudMLElementWithProperties(
    ) {
        super(
        );
        this.cloudml_puppetresources = new ArrayList<>();
        this.cloudml_propertys = new ArrayList<>();
        this.cloudml_resources = new ArrayList<>();
    }

    public cloudml_CloudMLElementWithProperties(
        ArrayList<cloudml_PuppetResource> cloudml_puppetresources,        ArrayList<cloudml_Property> cloudml_propertys,        ArrayList<cloudml_Resource> cloudml_resources    ) {
        this.cloudml_puppetresources = cloudml_puppetresources;
        this.cloudml_propertys = cloudml_propertys;
        this.cloudml_resources = cloudml_resources;
    }


    public List<cloudml_PuppetResource> getCloudml_puppetresources() {
        return cloudml_puppetresources;
    }

    public void addCloudml_puppetresource(Cloudml_puppetresource cloudml_puppetresource) {
        this.cloudml_puppetresources.add(cloudml_puppetresource);
    }
    public List<cloudml_Property> getCloudml_propertys() {
        return cloudml_propertys;
    }

    public void addCloudml_property(Cloudml_property cloudml_property) {
        this.cloudml_propertys.add(cloudml_property);
    }
    public List<cloudml_Resource> getCloudml_resources() {
        return cloudml_resources;
    }

    public void addCloudml_resource(Cloudml_resource cloudml_resource) {
        this.cloudml_resources.add(cloudml_resource);
    }

}