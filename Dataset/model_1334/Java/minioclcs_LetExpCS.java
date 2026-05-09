





import java.util.List;
import java.util.ArrayList;

public class minioclcs_LetExpCS extends PrimaryExpCS {






    private List<minioclcs_LetVarCS> minioclcs_letvarcss;




    private minioclcs_ExpCS minioclcs_expcs;


    public minioclcs_LetExpCS(
    ) {
        super(
        );
        this.minioclcs_letvarcss = new ArrayList<>();
    }

    public minioclcs_LetExpCS(
        ArrayList<minioclcs_LetVarCS> minioclcs_letvarcss    ) {
        this.minioclcs_letvarcss = minioclcs_letvarcss;
    }


    public List<minioclcs_LetVarCS> getMinioclcs_letvarcss() {
        return minioclcs_letvarcss;
    }

    public void addMinioclcs_letvarcs(Minioclcs_letvarcs minioclcs_letvarcs) {
        this.minioclcs_letvarcss.add(minioclcs_letvarcs);
    }
    public minioclcs_ExpCS getMinioclcs_expcs() {
        return minioclcs_expcs;
    }

    public void setMinioclcs_expcs(minioclcs_ExpCS minioclcs_expcs) {
        this.minioclcs_expcs = minioclcs_expcs;
    }

}