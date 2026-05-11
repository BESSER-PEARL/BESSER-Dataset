





import java.util.List;
import java.util.ArrayList;

public class iot_Transicion  {






    private iot_Dispositivo iot_dispositivo;




    private iot_Evento iot_evento;




    private iot_Estado iot_estado;


    public iot_Transicion(
    ) {
    }



    public iot_Dispositivo getIot_dispositivo() {
        return iot_dispositivo;
    }

    public void setIot_dispositivo(iot_Dispositivo iot_dispositivo) {
        this.iot_dispositivo = iot_dispositivo;
    }
    public iot_Evento getIot_evento() {
        return iot_evento;
    }

    public void setIot_evento(iot_Evento iot_evento) {
        this.iot_evento = iot_evento;
    }
    public iot_Estado getIot_estado() {
        return iot_estado;
    }

    public void setIot_estado(iot_Estado iot_estado) {
        this.iot_estado = iot_estado;
    }

}