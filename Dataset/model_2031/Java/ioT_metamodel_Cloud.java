





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Cloud  {






    private ioT_metamodel_Fog iot_metamodel_fog;




    private List<ioT_metamodel_Fog> iot_metamodel_fogs;


    public ioT_metamodel_Cloud(
    ) {
        this.iot_metamodel_fogs = new ArrayList<>();
    }

    public ioT_metamodel_Cloud(
        ArrayList<ioT_metamodel_Fog> iot_metamodel_fogs    ) {
        this.iot_metamodel_fogs = iot_metamodel_fogs;
    }


    public ioT_metamodel_Fog getIot_metamodel_fog() {
        return iot_metamodel_fog;
    }

    public void setIot_metamodel_fog(ioT_metamodel_Fog iot_metamodel_fog) {
        this.iot_metamodel_fog = iot_metamodel_fog;
    }
    public List<ioT_metamodel_Fog> getIot_metamodel_fogs() {
        return iot_metamodel_fogs;
    }

    public void addIot_metamodel_fog(Iot_metamodel_fog iot_metamodel_fog) {
        this.iot_metamodel_fogs.add(iot_metamodel_fog);
    }

}