





import java.util.List;
import java.util.ArrayList;

public class SmartHome_Room extends NamedElement {






    private SmartHome_Home smarthome_home;




    private SmartHome_Clock smarthome_clock;




    private List<SmartHome_Light> smarthome_lights;




    private SmartHome_Shutter smarthome_shutter;




    private SmartHome_PhysicalContext smarthome_physicalcontext;




    private List<SmartHome_Rule> smarthome_rules;




    private List<SmartHome_LightSensor> smarthome_lightsensors;


    public SmartHome_Room(
    ) {
        super(
        );
        this.smarthome_lights = new ArrayList<>();
        this.smarthome_rules = new ArrayList<>();
        this.smarthome_lightsensors = new ArrayList<>();
    }

    public SmartHome_Room(
        ArrayList<SmartHome_Light> smarthome_lights,        ArrayList<SmartHome_Rule> smarthome_rules,        ArrayList<SmartHome_LightSensor> smarthome_lightsensors    ) {
        this.smarthome_lights = smarthome_lights;
        this.smarthome_rules = smarthome_rules;
        this.smarthome_lightsensors = smarthome_lightsensors;
    }


    public SmartHome_Home getSmarthome_home() {
        return smarthome_home;
    }

    public void setSmarthome_home(SmartHome_Home smarthome_home) {
        this.smarthome_home = smarthome_home;
    }
    public SmartHome_Clock getSmarthome_clock() {
        return smarthome_clock;
    }

    public void setSmarthome_clock(SmartHome_Clock smarthome_clock) {
        this.smarthome_clock = smarthome_clock;
    }
    public List<SmartHome_Light> getSmarthome_lights() {
        return smarthome_lights;
    }

    public void addSmarthome_light(Smarthome_light smarthome_light) {
        this.smarthome_lights.add(smarthome_light);
    }
    public SmartHome_Shutter getSmarthome_shutter() {
        return smarthome_shutter;
    }

    public void setSmarthome_shutter(SmartHome_Shutter smarthome_shutter) {
        this.smarthome_shutter = smarthome_shutter;
    }
    public SmartHome_PhysicalContext getSmarthome_physicalcontext() {
        return smarthome_physicalcontext;
    }

    public void setSmarthome_physicalcontext(SmartHome_PhysicalContext smarthome_physicalcontext) {
        this.smarthome_physicalcontext = smarthome_physicalcontext;
    }
    public List<SmartHome_Rule> getSmarthome_rules() {
        return smarthome_rules;
    }

    public void addSmarthome_rule(Smarthome_rule smarthome_rule) {
        this.smarthome_rules.add(smarthome_rule);
    }
    public List<SmartHome_LightSensor> getSmarthome_lightsensors() {
        return smarthome_lightsensors;
    }

    public void addSmarthome_lightsensor(Smarthome_lightsensor smarthome_lightsensor) {
        this.smarthome_lightsensors.add(smarthome_lightsensor);
    }

}