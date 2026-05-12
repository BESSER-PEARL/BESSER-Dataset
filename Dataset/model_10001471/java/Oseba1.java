





import java.util.List;
import java.util.ArrayList;

public class Oseba1  {

    private String emso;
    private String ime;
    private String priimek;



    public Oseba1(
        String emso,        String ime,        String priimek    ) {
        this.emso = emso;
        this.ime = ime;
        this.priimek = priimek;
    }


    public String getEmso() {
        return emso;
    }

    public void setEmso(String emso) {
        this.emso = emso;
    }
    public String getIme() {
        return ime;
    }

    public void setIme(String ime) {
        this.ime = ime;
    }
    public String getPriimek() {
        return priimek;
    }

    public void setPriimek(String priimek) {
        this.priimek = priimek;
    }


}