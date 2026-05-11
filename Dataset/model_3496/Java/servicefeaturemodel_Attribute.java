





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_Attribute  {

    private String instantiationValue;
    private String id;



    public servicefeaturemodel_Attribute(
        String instantiationValue,        String id    ) {
        this.instantiationValue = instantiationValue;
        this.id = id;
    }


    public String getInstantiationvalue() {
        return instantiationValue;
    }

    public void setInstantiationvalue(String instantiationValue) {
        this.instantiationValue = instantiationValue;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}