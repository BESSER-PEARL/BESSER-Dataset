





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_InstallableUnits  {






    private Categories categories;




    private Bundles bundles;




    private List<IUPresentation> iupresentations;




    private Features features;




    private Fragments fragments;




    private Products products;


    public aggregator_p2view_InstallableUnits(
    ) {
        this.iupresentations = new ArrayList<>();
    }

    public aggregator_p2view_InstallableUnits(
        ArrayList<IUPresentation> iupresentations    ) {
        this.iupresentations = iupresentations;
    }


    public Categories getCategories() {
        return categories;
    }

    public void setCategories(Categories categories) {
        this.categories = categories;
    }
    public Bundles getBundles() {
        return bundles;
    }

    public void setBundles(Bundles bundles) {
        this.bundles = bundles;
    }
    public List<IUPresentation> getIupresentations() {
        return iupresentations;
    }

    public void addIupresentation(Iupresentation iupresentation) {
        this.iupresentations.add(iupresentation);
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
    public Products getProducts() {
        return products;
    }

    public void setProducts(Products products) {
        this.products = products;
    }

}