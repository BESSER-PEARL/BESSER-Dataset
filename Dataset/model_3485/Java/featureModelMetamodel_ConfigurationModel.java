





import java.util.List;
import java.util.ArrayList;

public class featureModelMetamodel_ConfigurationModel  {






    private List<featureModelMetamodel_Selection> featuremodelmetamodel_selections;


    public featureModelMetamodel_ConfigurationModel(
    ) {
        this.featuremodelmetamodel_selections = new ArrayList<>();
    }

    public featureModelMetamodel_ConfigurationModel(
        ArrayList<featureModelMetamodel_Selection> featuremodelmetamodel_selections    ) {
        this.featuremodelmetamodel_selections = featuremodelmetamodel_selections;
    }


    public List<featureModelMetamodel_Selection> getFeaturemodelmetamodel_selections() {
        return featuremodelmetamodel_selections;
    }

    public void addFeaturemodelmetamodel_selection(Featuremodelmetamodel_selection featuremodelmetamodel_selection) {
        this.featuremodelmetamodel_selections.add(featuremodelmetamodel_selection);
    }

}