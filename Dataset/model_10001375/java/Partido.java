





import java.util.List;
import java.util.ArrayList;

public class Partido  {

    private int resultado;
    private String localizaci_n;





    private List<Equipo> equipos;


    public Partido(
        int resultado,        String localizaci_n    ) {
        this.resultado = resultado;
        this.localizaci_n = localizaci_n;
        this.equipos = new ArrayList<>();
    }

    public Partido(
        int resultado,        String localizaci_n        ArrayList<Equipo> equipos    ) {
        this.resultado = resultado;
        this.localizaci_n = localizaci_n;
        this.equipos = equipos;
    }

    public int getResultado() {
        return resultado;
    }

    public void setResultado(int resultado) {
        this.resultado = resultado;
    }
    public String getLocalizaci_n() {
        return localizaci_n;
    }

    public void setLocalizaci_n(String localizaci_n) {
        this.localizaci_n = localizaci_n;
    }

    public List<Equipo> getEquipos() {
        return equipos;
    }

    public void addEquipo(Equipo equipo) {
        this.equipos.add(equipo);
    }

}