





import java.util.List;
import java.util.ArrayList;

public class iot_Etiqueta  {

    private String typeName;
    private String value;
    private String name;





    private iot_Dispositivo iot_dispositivo;


    public iot_Etiqueta(
        String typeName,        String value,        String name    ) {
        this.typeName = typeName;
        this.value = value;
        this.name = name;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iot_Dispositivo getIot_dispositivo() {
        return iot_dispositivo;
    }

    public void setIot_dispositivo(iot_Dispositivo iot_dispositivo) {
        this.iot_dispositivo = iot_dispositivo;
    }

}