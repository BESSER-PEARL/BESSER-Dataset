





import java.util.List;
import java.util.ArrayList;

public class occi_Configuration  {

    private String description;
    private String location;





    private List<occi_Extension> occi_extensions;




    private List<occi_Mixin> occi_mixins;




    private List<occi_Resource> occi_resources;


    public occi_Configuration(
        String description,        String location    ) {
        this.description = description;
        this.location = location;
        this.occi_extensions = new ArrayList<>();
        this.occi_mixins = new ArrayList<>();
        this.occi_resources = new ArrayList<>();
    }

    public occi_Configuration(
        String description,        String location        ArrayList<occi_Extension> occi_extensions,        ArrayList<occi_Mixin> occi_mixins,        ArrayList<occi_Resource> occi_resources    ) {
        this.description = description;
        this.location = location;
        this.occi_extensions = occi_extensions;
        this.occi_mixins = occi_mixins;
        this.occi_resources = occi_resources;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public List<occi_Extension> getOcci_extensions() {
        return occi_extensions;
    }

    public void addOcci_extension(Occi_extension occi_extension) {
        this.occi_extensions.add(occi_extension);
    }
    public List<occi_Mixin> getOcci_mixins() {
        return occi_mixins;
    }

    public void addOcci_mixin(Occi_mixin occi_mixin) {
        this.occi_mixins.add(occi_mixin);
    }
    public List<occi_Resource> getOcci_resources() {
        return occi_resources;
    }

    public void addOcci_resource(Occi_resource occi_resource) {
        this.occi_resources.add(occi_resource);
    }

}