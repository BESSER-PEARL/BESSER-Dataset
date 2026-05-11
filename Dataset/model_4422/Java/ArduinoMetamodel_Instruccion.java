





import java.util.List;
import java.util.ArrayList;

public class ArduinoMetamodel_Instruccion  {

    private String codigo;





    private ArduinoMetamodel_Metodo arduinometamodel_metodo;


    public ArduinoMetamodel_Instruccion(
        String codigo    ) {
        this.codigo = codigo;
    }


    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public ArduinoMetamodel_Metodo getArduinometamodel_metodo() {
        return arduinometamodel_metodo;
    }

    public void setArduinometamodel_metodo(ArduinoMetamodel_Metodo arduinometamodel_metodo) {
        this.arduinometamodel_metodo = arduinometamodel_metodo;
    }

}