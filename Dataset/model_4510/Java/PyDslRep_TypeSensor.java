





import java.util.List;
import java.util.ArrayList;

public class PyDslRep_TypeSensor extends Entity {

    private String typeName;



    public PyDslRep_TypeSensor(
        String typeName    ) {
        super(
        );
        this.typeName = typeName;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }


}