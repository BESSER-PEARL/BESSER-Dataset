





import java.util.List;
import java.util.ArrayList;

public class Partido  {

    private String idPartido;
    private String numeroApuestas;





    private List<Apuesta> apuestas;


    public Partido(
        String idPartido,        String numeroApuestas    ) {
        this.idPartido = idPartido;
        this.numeroApuestas = numeroApuestas;
        this.apuestas = new ArrayList<>();
    }

    public Partido(
        String idPartido,        String numeroApuestas        ArrayList<Apuesta> apuestas    ) {
        this.idPartido = idPartido;
        this.numeroApuestas = numeroApuestas;
        this.apuestas = apuestas;
    }

    public String getIdpartido() {
        return idPartido;
    }

    public void setIdpartido(String idPartido) {
        this.idPartido = idPartido;
    }
    public String getNumeroapuestas() {
        return numeroApuestas;
    }

    public void setNumeroapuestas(String numeroApuestas) {
        this.numeroApuestas = numeroApuestas;
    }

    public List<Apuesta> getApuestas() {
        return apuestas;
    }

    public void addApuesta(Apuesta apuesta) {
        this.apuestas.add(apuesta);
    }

}