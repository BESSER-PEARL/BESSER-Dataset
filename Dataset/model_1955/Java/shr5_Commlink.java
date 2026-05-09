





import java.util.List;
import java.util.ArrayList;

public class shr5_Commlink extends AbstractMatrixDevice {






    private List<shr5_Sin> shr5_sins;


    public shr5_Commlink(
    ) {
        super(
        );
        this.shr5_sins = new ArrayList<>();
    }

    public shr5_Commlink(
        ArrayList<shr5_Sin> shr5_sins    ) {
        this.shr5_sins = shr5_sins;
    }


    public List<shr5_Sin> getShr5_sins() {
        return shr5_sins;
    }

    public void addShr5_sin(Shr5_sin shr5_sin) {
        this.shr5_sins.add(shr5_sin);
    }

}