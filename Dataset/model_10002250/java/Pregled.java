





import java.util.List;
import java.util.ArrayList;

public class Pregled  {

    private String DatumP;
    private int BrPregled;





    private List<Lekar> lekars;


    public Pregled(
        String DatumP,        int BrPregled    ) {
        this.DatumP = DatumP;
        this.BrPregled = BrPregled;
        this.lekars = new ArrayList<>();
    }

    public Pregled(
        String DatumP,        int BrPregled        ArrayList<Lekar> lekars    ) {
        this.DatumP = DatumP;
        this.BrPregled = BrPregled;
        this.lekars = lekars;
    }

    public String getDatump() {
        return DatumP;
    }

    public void setDatump(String DatumP) {
        this.DatumP = DatumP;
    }
    public int getBrpregled() {
        return BrPregled;
    }

    public void setBrpregled(int BrPregled) {
        this.BrPregled = BrPregled;
    }

    public List<Lekar> getLekars() {
        return lekars;
    }

    public void addLekar(Lekar lekar) {
        this.lekars.add(lekar);
    }

}