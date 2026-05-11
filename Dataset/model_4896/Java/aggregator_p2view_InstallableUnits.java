





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_InstallableUnits  {






    private Features features;




    private List<IUPresentation> iupresentations;




    private Products products;




    private Miscellaneous miscellaneous;




    private Fragments fragments;




    private Bundles bundles;




    private Categories categories;


    public aggregator_p2view_InstallableUnits(
    ) {
        this.iupresentations = new ArrayList<>();
    }

    public aggregator_p2view_InstallableUnits(
        ArrayList<IUPresentation> iupresentations    ) {
        this.iupresentations = iupresentations;
    }


    public Features getFeatures() {
        return features;
    }

    public void setFeatures(Features features) {
        this.features = features;
    }
    public List<IUPresentation> getIupresentations() {
        return iupresentations;
    }

    public void addIupresentation(Iupresentation iupresentation) {
        this.iupresentations.add(iupresentation);
    }
    public Products getProducts() {
        return products;
    }

    public void setProducts(Products products) {
        this.products = products;
    }
    public Miscellaneous getMiscellaneous() {
        return miscellaneous;
    }

    public void setMiscellaneous(Miscellaneous miscellaneous) {
        this.miscellaneous = miscellaneous;
    }
    public Fragments getFragments() {
        return fragments;
    }

    public void setFragments(Fragments fragments) {
        this.fragments = fragments;
    }
    public Bundles getBundles() {
        return bundles;
    }

    public void setBundles(Bundles bundles) {
        this.bundles = bundles;
    }
    public Categories getCategories() {
        return categories;
    }

    public void setCategories(Categories categories) {
        this.categories = categories;
    }

}