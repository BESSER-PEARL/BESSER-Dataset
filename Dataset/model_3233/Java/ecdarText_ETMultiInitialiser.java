





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETMultiInitialiser extends ETInitialiser {






    private List<ecdarText_ETInitialiser> ecdartext_etinitialisers;


    public ecdarText_ETMultiInitialiser(
    ) {
        super(
        );
        this.ecdartext_etinitialisers = new ArrayList<>();
    }

    public ecdarText_ETMultiInitialiser(
        ArrayList<ecdarText_ETInitialiser> ecdartext_etinitialisers    ) {
        this.ecdartext_etinitialisers = ecdartext_etinitialisers;
    }


    public List<ecdarText_ETInitialiser> getEcdartext_etinitialisers() {
        return ecdartext_etinitialisers;
    }

    public void addEcdartext_etinitialiser(Ecdartext_etinitialiser ecdartext_etinitialiser) {
        this.ecdartext_etinitialisers.add(ecdartext_etinitialiser);
    }

}