





import java.util.List;
import java.util.ArrayList;

public class Transakcija  {

    private String suma;
    private String Trans_ID;
    private String tip;
    private String datum_trans;





    private List<Kupac> kupacs;


    public Transakcija(
        String suma,        String Trans_ID,        String tip,        String datum_trans    ) {
        this.suma = suma;
        this.Trans_ID = Trans_ID;
        this.tip = tip;
        this.datum_trans = datum_trans;
        this.kupacs = new ArrayList<>();
    }

    public Transakcija(
        String suma,        String Trans_ID,        String tip,        String datum_trans        ArrayList<Kupac> kupacs    ) {
        this.suma = suma;
        this.Trans_ID = Trans_ID;
        this.tip = tip;
        this.datum_trans = datum_trans;
        this.kupacs = kupacs;
    }

    public String getSuma() {
        return suma;
    }

    public void setSuma(String suma) {
        this.suma = suma;
    }
    public String getTrans_id() {
        return Trans_ID;
    }

    public void setTrans_id(String Trans_ID) {
        this.Trans_ID = Trans_ID;
    }
    public String getTip() {
        return tip;
    }

    public void setTip(String tip) {
        this.tip = tip;
    }
    public String getDatum_trans() {
        return datum_trans;
    }

    public void setDatum_trans(String datum_trans) {
        this.datum_trans = datum_trans;
    }

    public List<Kupac> getKupacs() {
        return kupacs;
    }

    public void addKupac(Kupac kupac) {
        this.kupacs.add(kupac);
    }

}