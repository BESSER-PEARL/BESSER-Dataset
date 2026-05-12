





import java.util.List;
import java.util.ArrayList;

public class Apuesta  {

    private String valorApuesta;
    private String porcentajeGanancia;
    private String id;





    private Usuario usuario;


    public Apuesta(
        String valorApuesta,        String porcentajeGanancia,        String id    ) {
        this.valorApuesta = valorApuesta;
        this.porcentajeGanancia = porcentajeGanancia;
        this.id = id;
    }


    public String getValorapuesta() {
        return valorApuesta;
    }

    public void setValorapuesta(String valorApuesta) {
        this.valorApuesta = valorApuesta;
    }
    public String getPorcentajeganancia() {
        return porcentajeGanancia;
    }

    public void setPorcentajeganancia(String porcentajeGanancia) {
        this.porcentajeGanancia = porcentajeGanancia;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

}