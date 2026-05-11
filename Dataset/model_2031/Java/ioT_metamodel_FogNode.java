





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_FogNode  {






    private ioT_metamodel_Fog iot_metamodel_fog;




    private ioT_metamodel_Analytics_Engine iot_metamodel_analytics_engine;




    private List<ioT_metamodel_VM> iot_metamodel_vms;




    private List<ioT_metamodel_Fog_Services> iot_metamodel_fog_servicess;




    private List<ioT_metamodel_Container> iot_metamodel_containers;


    public ioT_metamodel_FogNode(
    ) {
        this.iot_metamodel_vms = new ArrayList<>();
        this.iot_metamodel_fog_servicess = new ArrayList<>();
        this.iot_metamodel_containers = new ArrayList<>();
    }

    public ioT_metamodel_FogNode(
        ArrayList<ioT_metamodel_VM> iot_metamodel_vms,        ArrayList<ioT_metamodel_Fog_Services> iot_metamodel_fog_servicess,        ArrayList<ioT_metamodel_Container> iot_metamodel_containers    ) {
        this.iot_metamodel_vms = iot_metamodel_vms;
        this.iot_metamodel_fog_servicess = iot_metamodel_fog_servicess;
        this.iot_metamodel_containers = iot_metamodel_containers;
    }


    public ioT_metamodel_Fog getIot_metamodel_fog() {
        return iot_metamodel_fog;
    }

    public void setIot_metamodel_fog(ioT_metamodel_Fog iot_metamodel_fog) {
        this.iot_metamodel_fog = iot_metamodel_fog;
    }
    public ioT_metamodel_Analytics_Engine getIot_metamodel_analytics_engine() {
        return iot_metamodel_analytics_engine;
    }

    public void setIot_metamodel_analytics_engine(ioT_metamodel_Analytics_Engine iot_metamodel_analytics_engine) {
        this.iot_metamodel_analytics_engine = iot_metamodel_analytics_engine;
    }
    public List<ioT_metamodel_VM> getIot_metamodel_vms() {
        return iot_metamodel_vms;
    }

    public void addIot_metamodel_vm(Iot_metamodel_vm iot_metamodel_vm) {
        this.iot_metamodel_vms.add(iot_metamodel_vm);
    }
    public List<ioT_metamodel_Fog_Services> getIot_metamodel_fog_servicess() {
        return iot_metamodel_fog_servicess;
    }

    public void addIot_metamodel_fog_services(Iot_metamodel_fog_services iot_metamodel_fog_services) {
        this.iot_metamodel_fog_servicess.add(iot_metamodel_fog_services);
    }
    public List<ioT_metamodel_Container> getIot_metamodel_containers() {
        return iot_metamodel_containers;
    }

    public void addIot_metamodel_container(Iot_metamodel_container iot_metamodel_container) {
        this.iot_metamodel_containers.add(iot_metamodel_container);
    }

}