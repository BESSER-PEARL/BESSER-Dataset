





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Operations  {






    private List<ioT_metamodel_InformationResource> iot_metamodel_informationresources;




    private ioT_metamodel_Container iot_metamodel_container;




    private ioT_metamodel_Fog_Services iot_metamodel_fog_services;


    public ioT_metamodel_Operations(
    ) {
        this.iot_metamodel_informationresources = new ArrayList<>();
    }

    public ioT_metamodel_Operations(
        ArrayList<ioT_metamodel_InformationResource> iot_metamodel_informationresources    ) {
        this.iot_metamodel_informationresources = iot_metamodel_informationresources;
    }


    public List<ioT_metamodel_InformationResource> getIot_metamodel_informationresources() {
        return iot_metamodel_informationresources;
    }

    public void addIot_metamodel_informationresource(Iot_metamodel_informationresource iot_metamodel_informationresource) {
        this.iot_metamodel_informationresources.add(iot_metamodel_informationresource);
    }
    public ioT_metamodel_Container getIot_metamodel_container() {
        return iot_metamodel_container;
    }

    public void setIot_metamodel_container(ioT_metamodel_Container iot_metamodel_container) {
        this.iot_metamodel_container = iot_metamodel_container;
    }
    public ioT_metamodel_Fog_Services getIot_metamodel_fog_services() {
        return iot_metamodel_fog_services;
    }

    public void setIot_metamodel_fog_services(ioT_metamodel_Fog_Services iot_metamodel_fog_services) {
        this.iot_metamodel_fog_services = iot_metamodel_fog_services;
    }

}