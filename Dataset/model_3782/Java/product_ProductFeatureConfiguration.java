





import java.util.List;
import java.util.ArrayList;

public class product_ProductFeatureConfiguration  {

    private String name;
    private int min;
    private int max;
    private String attribute;
    private boolean isSelected;





    private List<product_ProductFeatureConfiguration> product_productfeatureconfigurations;




    private product_ProductFeaturesConfiguration product_productfeaturesconfiguration;


    public product_ProductFeatureConfiguration(
        String name,        int min,        int max,        String attribute,        boolean isSelected    ) {
        this.name = name;
        this.min = min;
        this.max = max;
        this.attribute = attribute;
        this.isSelected = isSelected;
        this.product_productfeatureconfigurations = new ArrayList<>();
    }

    public product_ProductFeatureConfiguration(
        String name,        int min,        int max,        String attribute,        boolean isSelected        ArrayList<product_ProductFeatureConfiguration> product_productfeatureconfigurations    ) {
        this.name = name;
        this.min = min;
        this.max = max;
        this.attribute = attribute;
        this.isSelected = isSelected;
        this.product_productfeatureconfigurations = product_productfeatureconfigurations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public boolean getIsselected() {
        return isSelected;
    }

    public void setIsselected(boolean isSelected) {
        this.isSelected = isSelected;
    }

    public List<product_ProductFeatureConfiguration> getProduct_productfeatureconfigurations() {
        return product_productfeatureconfigurations;
    }

    public void addProduct_productfeatureconfiguration(Product_productfeatureconfiguration product_productfeatureconfiguration) {
        this.product_productfeatureconfigurations.add(product_productfeatureconfiguration);
    }
    public product_ProductFeaturesConfiguration getProduct_productfeaturesconfiguration() {
        return product_productfeaturesconfiguration;
    }

    public void setProduct_productfeaturesconfiguration(product_ProductFeaturesConfiguration product_productfeaturesconfiguration) {
        this.product_productfeaturesconfiguration = product_productfeaturesconfiguration;
    }

}