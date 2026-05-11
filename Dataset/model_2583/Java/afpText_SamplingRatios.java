





import java.util.List;
import java.util.ArrayList;

public class afpText_SamplingRatios extends triplet {






    private List<afpText_SamplingRatiosRG> afptext_samplingratiosrgs;


    public afpText_SamplingRatios(
    ) {
        super(
        );
        this.afptext_samplingratiosrgs = new ArrayList<>();
    }

    public afpText_SamplingRatios(
        ArrayList<afpText_SamplingRatiosRG> afptext_samplingratiosrgs    ) {
        this.afptext_samplingratiosrgs = afptext_samplingratiosrgs;
    }


    public List<afpText_SamplingRatiosRG> getAfptext_samplingratiosrgs() {
        return afptext_samplingratiosrgs;
    }

    public void addAfptext_samplingratiosrg(Afptext_samplingratiosrg afptext_samplingratiosrg) {
        this.afptext_samplingratiosrgs.add(afptext_samplingratiosrg);
    }

}