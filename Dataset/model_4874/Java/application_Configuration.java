





import java.util.List;
import java.util.ArrayList;

public class application_Configuration  {






    private List<application_Property> application_propertys;


    public application_Configuration(
    ) {
        this.application_propertys = new ArrayList<>();
    }

    public application_Configuration(
        ArrayList<application_Property> application_propertys    ) {
        this.application_propertys = application_propertys;
    }


    public List<application_Property> getApplication_propertys() {
        return application_propertys;
    }

    public void addApplication_property(Application_property application_property) {
        this.application_propertys.add(application_property);
    }

}