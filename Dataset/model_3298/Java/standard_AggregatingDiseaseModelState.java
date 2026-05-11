





import java.util.List;
import java.util.ArrayList;

public class standard_AggregatingDiseaseModelState extends DiseaseModelState {






    private List<standard_SILabel> standard_silabels;


    public standard_AggregatingDiseaseModelState(
    ) {
        super(
        );
        this.standard_silabels = new ArrayList<>();
    }

    public standard_AggregatingDiseaseModelState(
        ArrayList<standard_SILabel> standard_silabels    ) {
        this.standard_silabels = standard_silabels;
    }


    public List<standard_SILabel> getStandard_silabels() {
        return standard_silabels;
    }

    public void addStandard_silabel(Standard_silabel standard_silabel) {
        this.standard_silabels.add(standard_silabel);
    }

}