





import java.util.List;
import java.util.ArrayList;

public class Pes  {

    private String vzdevek;
    private String pasma;
    private String visina;



    public Pes(
        String vzdevek,        String pasma,        String visina    ) {
        this.vzdevek = vzdevek;
        this.pasma = pasma;
        this.visina = visina;
    }


    public String getVzdevek() {
        return vzdevek;
    }

    public void setVzdevek(String vzdevek) {
        this.vzdevek = vzdevek;
    }
    public String getPasma() {
        return pasma;
    }

    public void setPasma(String pasma) {
        this.pasma = pasma;
    }
    public String getVisina() {
        return visina;
    }

    public void setVisina(String visina) {
        this.visina = visina;
    }


}