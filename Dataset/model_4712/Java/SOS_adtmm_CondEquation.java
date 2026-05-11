





import java.util.List;
import java.util.ArrayList;

public class SOS_adtmm_CondEquation  {






    private List<AbstractEquation> abstractequations;


    public SOS_adtmm_CondEquation(
    ) {
        this.abstractequations = new ArrayList<>();
    }

    public SOS_adtmm_CondEquation(
        ArrayList<AbstractEquation> abstractequations    ) {
        this.abstractequations = abstractequations;
    }


    public List<AbstractEquation> getAbstractequations() {
        return abstractequations;
    }

    public void addAbstractequation(Abstractequation abstractequation) {
        this.abstractequations.add(abstractequation);
    }

}