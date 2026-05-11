





import java.util.List;
import java.util.ArrayList;

public class cloudml_WithProperties extends NamedElement {






    private List<cloudml_Property> cloudml_propertys;


    public cloudml_WithProperties(
    ) {
        super(
        );
        this.cloudml_propertys = new ArrayList<>();
    }

    public cloudml_WithProperties(
        ArrayList<cloudml_Property> cloudml_propertys    ) {
        this.cloudml_propertys = cloudml_propertys;
    }


    public List<cloudml_Property> getCloudml_propertys() {
        return cloudml_propertys;
    }

    public void addCloudml_property(Cloudml_property cloudml_property) {
        this.cloudml_propertys.add(cloudml_property);
    }

}