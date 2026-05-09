





import java.util.List;
import java.util.ArrayList;

public class shr5_Magazin extends Capacity, AbstraktGegenstand {






    private List<shr5_Munition> shr5_munitions;


    public shr5_Magazin(
    ) {
        super(
        );
        this.shr5_munitions = new ArrayList<>();
    }

    public shr5_Magazin(
        ArrayList<shr5_Munition> shr5_munitions    ) {
        this.shr5_munitions = shr5_munitions;
    }


    public List<shr5_Munition> getShr5_munitions() {
        return shr5_munitions;
    }

    public void addShr5_munition(Shr5_munition shr5_munition) {
        this.shr5_munitions.add(shr5_munition);
    }

}