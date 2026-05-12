





import java.util.List;
import java.util.ArrayList;

public class retard  {

    private int idretad;
    private int nbrminute;
    private String motif;





    private Employ_ employ_;


    public retard(
        int idretad,        int nbrminute,        String motif    ) {
        this.idretad = idretad;
        this.nbrminute = nbrminute;
        this.motif = motif;
    }


    public int getIdretad() {
        return idretad;
    }

    public void setIdretad(int idretad) {
        this.idretad = idretad;
    }
    public int getNbrminute() {
        return nbrminute;
    }

    public void setNbrminute(int nbrminute) {
        this.nbrminute = nbrminute;
    }
    public String getMotif() {
        return motif;
    }

    public void setMotif(String motif) {
        this.motif = motif;
    }

    public Employ_ getEmploy_() {
        return employ_;
    }

    public void setEmploy_(Employ_ employ_) {
        this.employ_ = employ_;
    }

}