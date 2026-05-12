





import java.util.List;
import java.util.ArrayList;

public class Nilai  {

    private int tugas;
    private int uas;
    private String namaMK;
    private int uts;





    private Mahasiswa mahasiswa;


    public Nilai(
        int tugas,        int uas,        String namaMK,        int uts    ) {
        this.tugas = tugas;
        this.uas = uas;
        this.namaMK = namaMK;
        this.uts = uts;
    }


    public int getTugas() {
        return tugas;
    }

    public void setTugas(int tugas) {
        this.tugas = tugas;
    }
    public int getUas() {
        return uas;
    }

    public void setUas(int uas) {
        this.uas = uas;
    }
    public String getNamamk() {
        return namaMK;
    }

    public void setNamamk(String namaMK) {
        this.namaMK = namaMK;
    }
    public int getUts() {
        return uts;
    }

    public void setUts(int uts) {
        this.uts = uts;
    }

    public Mahasiswa getMahasiswa() {
        return mahasiswa;
    }

    public void setMahasiswa(Mahasiswa mahasiswa) {
        this.mahasiswa = mahasiswa;
    }

}