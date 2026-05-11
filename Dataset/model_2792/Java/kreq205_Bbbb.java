





import java.util.List;
import java.util.ArrayList;

public class kreq205_Bbbb  {






    private List<kreq205_Rrrr> kreq205_rrrrs;




    private List<kreq205_Cccc> kreq205_ccccs;




    private List<kreq205_Tttt> kreq205_tttts;


    public kreq205_Bbbb(
    ) {
        this.kreq205_rrrrs = new ArrayList<>();
        this.kreq205_ccccs = new ArrayList<>();
        this.kreq205_tttts = new ArrayList<>();
    }

    public kreq205_Bbbb(
        ArrayList<kreq205_Rrrr> kreq205_rrrrs,        ArrayList<kreq205_Cccc> kreq205_ccccs,        ArrayList<kreq205_Tttt> kreq205_tttts    ) {
        this.kreq205_rrrrs = kreq205_rrrrs;
        this.kreq205_ccccs = kreq205_ccccs;
        this.kreq205_tttts = kreq205_tttts;
    }


    public List<kreq205_Rrrr> getKreq205_rrrrs() {
        return kreq205_rrrrs;
    }

    public void addKreq205_rrrr(Kreq205_rrrr kreq205_rrrr) {
        this.kreq205_rrrrs.add(kreq205_rrrr);
    }
    public List<kreq205_Cccc> getKreq205_ccccs() {
        return kreq205_ccccs;
    }

    public void addKreq205_cccc(Kreq205_cccc kreq205_cccc) {
        this.kreq205_ccccs.add(kreq205_cccc);
    }
    public List<kreq205_Tttt> getKreq205_tttts() {
        return kreq205_tttts;
    }

    public void addKreq205_tttt(Kreq205_tttt kreq205_tttt) {
        this.kreq205_tttts.add(kreq205_tttt);
    }

}