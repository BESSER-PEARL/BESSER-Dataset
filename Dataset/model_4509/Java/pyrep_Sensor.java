





import java.util.List;
import java.util.ArrayList;

public class pyrep_Sensor extends Entity {

    private String name;





    private pyrep_TypeSensor pyrep_typesensor;


    public pyrep_Sensor(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pyrep_TypeSensor getPyrep_typesensor() {
        return pyrep_typesensor;
    }

    public void setPyrep_typesensor(pyrep_TypeSensor pyrep_typesensor) {
        this.pyrep_typesensor = pyrep_typesensor;
    }

}