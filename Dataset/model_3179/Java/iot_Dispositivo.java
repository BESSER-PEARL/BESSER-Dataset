





import java.util.List;
import java.util.ArrayList;

public class iot_Dispositivo  {

    private String name;





    private iot_Dispositivo iot_dispositivo;




    private List<iot_Evento> iot_eventos;




    private List<iot_Estado> iot_estados;




    private iot_Model iot_model;


    public iot_Dispositivo(
        String name    ) {
        this.name = name;
        this.iot_eventos = new ArrayList<>();
        this.iot_estados = new ArrayList<>();
    }

    public iot_Dispositivo(
        String name        ArrayList<iot_Evento> iot_eventos,        ArrayList<iot_Estado> iot_estados    ) {
        this.name = name;
        this.iot_eventos = iot_eventos;
        this.iot_estados = iot_estados;
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
    public List<iot_Evento> getIot_eventos() {
        return iot_eventos;
    }

    public void addIot_evento(Iot_evento iot_evento) {
        this.iot_eventos.add(iot_evento);
    }
    public List<iot_Estado> getIot_estados() {
        return iot_estados;
    }

    public void addIot_estado(Iot_estado iot_estado) {
        this.iot_estados.add(iot_estado);
    }
    public iot_Model getIot_model() {
        return iot_model;
    }

    public void setIot_model(iot_Model iot_model) {
        this.iot_model = iot_model;
    }

}