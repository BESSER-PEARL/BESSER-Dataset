





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_Category extends IUPresentation {






    private Bundles bundles;




    private Products products;




    private Categories categories;




    private IUDetails iudetails;




    private Fragments fragments;




    private Features features;


    public aggregator_p2view_Category(
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
    public Products getProducts() {
        return products;
    }

    public void setProducts(Products products) {
        this.products = products;
    }
    public Categories getCategories() {
        return categories;
    }

    public void setCategories(Categories categories) {
        this.categories = categories;
    }
    public IUDetails getIudetails() {
        return iudetails;
    }

    public void setIudetails(IUDetails iudetails) {
        this.iudetails = iudetails;
    }
    public Fragments getFragments() {
        return fragments;
    }

    public void setFragments(Fragments fragments) {
        this.fragments = fragments;
    }
    public Features getFeatures() {
        return features;
    }

    public void setFeatures(Features features) {
        this.features = features;
    }

}