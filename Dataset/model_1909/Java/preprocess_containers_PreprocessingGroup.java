





import java.util.List;
import java.util.ArrayList;

public class preprocess_containers_PreprocessingGroup extends CobolRoot {






    private List<PreprocessingUnit> preprocessingunits;


    public preprocess_containers_PreprocessingGroup(
    ) {
        super(
        );
        this.preprocessingunits = new ArrayList<>();
    }

    public preprocess_containers_PreprocessingGroup(
        ArrayList<PreprocessingUnit> preprocessingunits    ) {
        this.preprocessingunits = preprocessingunits;
    }


    public List<PreprocessingUnit> getPreprocessingunits() {
        return preprocessingunits;
    }

    public void addPreprocessingunit(Preprocessingunit preprocessingunit) {
        this.preprocessingunits.add(preprocessingunit);
    }

}