





import java.util.List;
import java.util.ArrayList;

public class abs  {

    private int nbrjr;
    private int idab;
    private String motif;





    private Employ_ employ_;


    public abs(
        int nbrjr,        int idab,        String motif    ) {
        this.nbrjr = nbrjr;
        this.idab = idab;
        this.motif = motif;
    }


    public int getNbrjr() {
        return nbrjr;
    }

    public void setNbrjr(int nbrjr) {
        this.nbrjr = nbrjr;
    }
    public int getIdab() {
        return idab;
    }

    public void setIdab(int idab) {
        this.idab = idab;
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