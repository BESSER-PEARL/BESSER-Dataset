





import java.util.List;
import java.util.ArrayList;

public class iot_Evento  {

    private String typeName;
    private String name;



    public iot_Evento(
        String typeName,        String name    ) {
        this.typeName = typeName;
        this.name = name;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}