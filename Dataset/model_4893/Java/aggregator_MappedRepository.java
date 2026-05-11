





import java.util.List;
import java.util.ArrayList;

public class aggregator_MappedRepository extends DescriptionProvider, MetadataRepositoryReference {

    private String categoryPrefix;
    private boolean mirrorArtifacts;





    private List<aggregator_Feature> aggregator_features;




    private List<aggregator_Bundle> aggregator_bundles;




    private List<aggregator_MapRule> aggregator_maprules;




    private aggregator_Contribution aggregator_contribution;




    private List<aggregator_Product> aggregator_products;




    private List<aggregator_Category> aggregator_categorys;


    public aggregator_MappedRepository(
        String categoryPrefix,        boolean mirrorArtifacts    ) {
        super(
        );
        this.categoryPrefix = categoryPrefix;
        this.mirrorArtifacts = mirrorArtifacts;
        this.aggregator_features = new ArrayList<>();
        this.aggregator_bundles = new ArrayList<>();
        this.aggregator_maprules = new ArrayList<>();
        this.aggregator_products = new ArrayList<>();
        this.aggregator_categorys = new ArrayList<>();
    }

    public aggregator_MappedRepository(
        String categoryPrefix,        boolean mirrorArtifacts        ArrayList<aggregator_Feature> aggregator_features,        ArrayList<aggregator_Bundle> aggregator_bundles,        ArrayList<aggregator_MapRule> aggregator_maprules,        ArrayList<aggregator_Product> aggregator_products,        ArrayList<aggregator_Category> aggregator_categorys    ) {
        this.categoryPrefix = categoryPrefix;
        this.mirrorArtifacts = mirrorArtifacts;
        this.aggregator_features = aggregator_features;
        this.aggregator_bundles = aggregator_bundles;
        this.aggregator_maprules = aggregator_maprules;
        this.aggregator_products = aggregator_products;
        this.aggregator_categorys = aggregator_categorys;
    }

    public String getCategoryprefix() {
        return categoryPrefix;
    }

    public void setCategoryprefix(String categoryPrefix) {
        this.categoryPrefix = categoryPrefix;
    }
    public boolean getMirrorartifacts() {
        return mirrorArtifacts;
    }

    public void setMirrorartifacts(boolean mirrorArtifacts) {
        this.mirrorArtifacts = mirrorArtifacts;
    }

    public List<aggregator_Feature> getAggregator_features() {
        return aggregator_features;
    }

    public void addAggregator_feature(Aggregator_feature aggregator_feature) {
        this.aggregator_features.add(aggregator_feature);
    }
    public List<aggregator_Bundle> getAggregator_bundles() {
        return aggregator_bundles;
    }

    public void addAggregator_bundle(Aggregator_bundle aggregator_bundle) {
        this.aggregator_bundles.add(aggregator_bundle);
    }
    public List<aggregator_MapRule> getAggregator_maprules() {
        return aggregator_maprules;
    }

    public void addAggregator_maprule(Aggregator_maprule aggregator_maprule) {
        this.aggregator_maprules.add(aggregator_maprule);
    }
    public aggregator_Contribution getAggregator_contribution() {
        return aggregator_contribution;
    }

    public void setAggregator_contribution(aggregator_Contribution aggregator_contribution) {
        this.aggregator_contribution = aggregator_contribution;
    }
    public List<aggregator_Product> getAggregator_products() {
        return aggregator_products;
    }

    public void addAggregator_product(Aggregator_product aggregator_product) {
        this.aggregator_products.add(aggregator_product);
    }
    public List<aggregator_Category> getAggregator_categorys() {
        return aggregator_categorys;
    }

    public void addAggregator_category(Aggregator_category aggregator_category) {
        this.aggregator_categorys.add(aggregator_category);
    }

}