





import java.util.List;
import java.util.ArrayList;

public class shr5Management_Pack extends Quelle, Beschreibbar, GeldWert {






    private List<shr5Management_Quelle> shr5management_quelles;


    public shr5Management_Pack(
    ) {
        super(
        );
        this.shr5management_quelles = new ArrayList<>();
    }

    public shr5Management_Pack(
        ArrayList<shr5Management_Quelle> shr5management_quelles    ) {
        this.shr5management_quelles = shr5management_quelles;
    }


    public List<shr5Management_Quelle> getShr5management_quelles() {
        return shr5management_quelles;
    }

    public void addShr5management_quelle(Shr5management_quelle shr5management_quelle) {
        this.shr5management_quelles.add(shr5management_quelle);
    }

}