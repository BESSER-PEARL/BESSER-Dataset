





import java.util.List;
import java.util.ArrayList;

public class camel_metric_Property  {

    private String type;
    private String name;
    private String description;





    private List<Sensor> sensors;




    private List<Property> propertys;


    public camel_metric_Property(
        String type,        String name,        String description    ) {
        this.type = type;
        this.name = name;
        this.description = description;
        this.sensors = new ArrayList<>();
        this.propertys = new ArrayList<>();
    }

    public camel_metric_Property(
        String type,        String name,        String description        ArrayList<Sensor> sensors,        ArrayList<Property> propertys    ) {
        this.type = type;
        this.name = name;
        this.description = description;
        this.sensors = sensors;
        this.propertys = propertys;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Sensor> getSensors() {
        return sensors;
    }

    public void addSensor(Sensor sensor) {
        this.sensors.add(sensor);
    }
    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}