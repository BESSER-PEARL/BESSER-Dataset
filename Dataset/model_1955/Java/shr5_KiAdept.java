





import java.util.List;
import java.util.ArrayList;

public class shr5_KiAdept extends MagischePersona {






    private List<shr5_KiKraft> shr5_kikrafts;


    public shr5_KiAdept(
    ) {
        super(
        );
        this.shr5_kikrafts = new ArrayList<>();
    }

    public shr5_KiAdept(
        ArrayList<shr5_KiKraft> shr5_kikrafts    ) {
        this.shr5_kikrafts = shr5_kikrafts;
    }


    public List<shr5_KiKraft> getShr5_kikrafts() {
        return shr5_kikrafts;
    }

    public void addShr5_kikraft(Shr5_kikraft shr5_kikraft) {
        this.shr5_kikrafts.add(shr5_kikraft);
    }

}