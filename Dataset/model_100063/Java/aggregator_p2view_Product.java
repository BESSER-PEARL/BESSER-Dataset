





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_Product extends IUPresentationWithDetails {






    private Bundles bundles;




    private Features features;




    private Fragments fragments;


    public aggregator_p2view_Product(
    ) {
        super(
        );
    }



    public Bundles getBundles() {
        return bundles;
    }

    public void setBundles(Bundles bundles) {
        this.bundles = bundles;
    }
    public Features getFeatures() {
        return features;
    }

    public void setFeatures(Features features) {
        this.features = features;
    }
    public Fragments getFragments() {
        return fragments;
    }

    public void setFragments(Fragments fragments) {
        this.fragments = fragments;
    }

}