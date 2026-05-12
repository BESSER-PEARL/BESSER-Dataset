





import java.util.List;
import java.util.ArrayList;

public class Arbitro  {

    private String Cod_persona;
    private String Partidos;
    private String Cod_Arbitro;



    public Arbitro(
        String Cod_persona,        String Partidos,        String Cod_Arbitro    ) {
        this.Cod_persona = Cod_persona;
        this.Partidos = Partidos;
        this.Cod_Arbitro = Cod_Arbitro;
    }


    public String getCod_persona() {
        return Cod_persona;
    }

    public void setCod_persona(String Cod_persona) {
        this.Cod_persona = Cod_persona;
    }
    public String getPartidos() {
        return Partidos;
    }

    public void setPartidos(String Partidos) {
        this.Partidos = Partidos;
    }
    public String getCod_arbitro() {
        return Cod_Arbitro;
    }

    public void setCod_arbitro(String Cod_Arbitro) {
        this.Cod_Arbitro = Cod_Arbitro;
    }


}