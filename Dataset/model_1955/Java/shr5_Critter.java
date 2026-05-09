





import java.util.List;
import java.util.ArrayList;

public class shr5_Critter extends Spezies {






    private List<shr5_CritterKraft> shr5_critterkrafts;


    public shr5_Critter(
    ) {
        super(
        );
        this.shr5_critterkrafts = new ArrayList<>();
    }

    public shr5_Critter(
        ArrayList<shr5_CritterKraft> shr5_critterkrafts    ) {
        this.shr5_critterkrafts = shr5_critterkrafts;
    }


    public List<shr5_CritterKraft> getShr5_critterkrafts() {
        return shr5_critterkrafts;
    }

    public void addShr5_critterkraft(Shr5_critterkraft shr5_critterkraft) {
        this.shr5_critterkrafts.add(shr5_critterkraft);
    }

}