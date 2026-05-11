





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Fog_Services  {






    private ioT_metamodel_Container iot_metamodel_container;




    private ioT_metamodel_Fog_Services iot_metamodel_fog_services;




    private List<ioT_metamodel_VirtualThing> iot_metamodel_virtualthings;




    private ioT_metamodel_User iot_metamodel_user;




    private List<ioT_metamodel_InformationResource> iot_metamodel_informationresources;


    public ioT_metamodel_Fog_Services(
    ) {
        this.iot_metamodel_virtualthings = new ArrayList<>();
        this.iot_metamodel_informationresources = new ArrayList<>();
    }

    public ioT_metamodel_Fog_Services(
        ArrayList<ioT_metamodel_VirtualThing> iot_metamodel_virtualthings,        ArrayList<ioT_metamodel_InformationResource> iot_metamodel_informationresources    ) {
        this.iot_metamodel_virtualthings = iot_metamodel_virtualthings;
        this.iot_metamodel_informationresources = iot_metamodel_informationresources;
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
    public List<ioT_metamodel_VirtualThing> getIot_metamodel_virtualthings() {
        return iot_metamodel_virtualthings;
    }

    public void addIot_metamodel_virtualthing(Iot_metamodel_virtualthing iot_metamodel_virtualthing) {
        this.iot_metamodel_virtualthings.add(iot_metamodel_virtualthing);
    }
    public ioT_metamodel_User getIot_metamodel_user() {
        return iot_metamodel_user;
    }

    public void setIot_metamodel_user(ioT_metamodel_User iot_metamodel_user) {
        this.iot_metamodel_user = iot_metamodel_user;
    }
    public List<ioT_metamodel_InformationResource> getIot_metamodel_informationresources() {
        return iot_metamodel_informationresources;
    }

    public void addIot_metamodel_informationresource(Iot_metamodel_informationresource iot_metamodel_informationresource) {
        this.iot_metamodel_informationresources.add(iot_metamodel_informationresource);
    }

}