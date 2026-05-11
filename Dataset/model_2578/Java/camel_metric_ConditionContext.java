





import java.util.List;
import java.util.ArrayList;

public class camel_metric_ConditionContext  {

    private float maxQuantity;
    private float minQuantity;
    private boolean isRelative;
    private String name;
    private String quantifier;





    private Component component;


    public camel_metric_ConditionContext(
        float maxQuantity,        float minQuantity,        boolean isRelative,        String name,        String quantifier    ) {
        this.maxQuantity = maxQuantity;
        this.minQuantity = minQuantity;
        this.isRelative = isRelative;
        this.name = name;
        this.quantifier = quantifier;
    }


    public float getMaxquantity() {
        return maxQuantity;
    }

    public void setMaxquantity(float maxQuantity) {
        this.maxQuantity = maxQuantity;
    }
    public float getMinquantity() {
        return minQuantity;
    }

    public void setMinquantity(float minQuantity) {
        this.minQuantity = minQuantity;
    }
    public boolean getIsrelative() {
        return isRelative;
    }

    public void setIsrelative(boolean isRelative) {
        this.isRelative = isRelative;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQuantifier() {
        return quantifier;
    }

    public void setQuantifier(String quantifier) {
        this.quantifier = quantifier;
    }

    public Component getComponent() {
        return component;
    }

    public void setComponent(Component component) {
        this.component = component;
    }

}