





import java.util.List;
import java.util.ArrayList;

public class PyDslRep_Sensor extends Entity {

    private String name;





    private PyDslRep_TypeSensor pydslrep_typesensor;


    public PyDslRep_Sensor(
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

    public PyDslRep_TypeSensor getPydslrep_typesensor() {
        return pydslrep_typesensor;
    }

    public void setPydslrep_typesensor(PyDslRep_TypeSensor pydslrep_typesensor) {
        this.pydslrep_typesensor = pydslrep_typesensor;
    }

}