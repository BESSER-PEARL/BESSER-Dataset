





import java.util.List;
import java.util.ArrayList;

public class DAO_Nilai  {

    private String tugas;
    private String uts;
    private String uas;
    private String namaMk;





    private Nilai nilai;


    public DAO_Nilai(
        String tugas,        String uts,        String uas,        String namaMk    ) {
        this.tugas = tugas;
        this.uts = uts;
        this.uas = uas;
        this.namaMk = namaMk;
    }


    public String getTugas() {
        return tugas;
    }

    public void setTugas(String tugas) {
        this.tugas = tugas;
    }
    public String getUts() {
        return uts;
    }

    public void setUts(String uts) {
        this.uts = uts;
    }
    public String getUas() {
        return uas;
    }

    public void setUas(String uas) {
        this.uas = uas;
    }
    public String getNamamk() {
        return namaMk;
    }

    public void setNamamk(String namaMk) {
        this.namaMk = namaMk;
    }

    public Nilai getNilai() {
        return nilai;
    }

    public void setNilai(Nilai nilai) {
        this.nilai = nilai;
    }

}