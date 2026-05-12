





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String studijskiProgram;
    private None datumVpisa;
    private String vpisnaStevilka;



    public Student(
        String studijskiProgram,        None datumVpisa,        String vpisnaStevilka    ) {
        this.studijskiProgram = studijskiProgram;
        this.datumVpisa = datumVpisa;
        this.vpisnaStevilka = vpisnaStevilka;
    }


    public String getStudijskiprogram() {
        return studijskiProgram;
    }

    public void setStudijskiprogram(String studijskiProgram) {
        this.studijskiProgram = studijskiProgram;
    }
    public None getDatumvpisa() {
        return datumVpisa;
    }

    public void setDatumvpisa(None datumVpisa) {
        this.datumVpisa = datumVpisa;
    }
    public String getVpisnastevilka() {
        return vpisnaStevilka;
    }

    public void setVpisnastevilka(String vpisnaStevilka) {
        this.vpisnaStevilka = vpisnaStevilka;
    }


}