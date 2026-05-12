





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int privateAttribute;
    private String packageAttribute;
    private float publicAttribute;
    private String protectedAttribute;



    public Product(
        int privateAttribute,        String packageAttribute,        float publicAttribute,        String protectedAttribute    ) {
        this.privateAttribute = privateAttribute;
        this.packageAttribute = packageAttribute;
        this.publicAttribute = publicAttribute;
        this.protectedAttribute = protectedAttribute;
    }


    public int getPrivateattribute() {
        return privateAttribute;
    }

    public void setPrivateattribute(int privateAttribute) {
        this.privateAttribute = privateAttribute;
    }
    public String getPackageattribute() {
        return packageAttribute;
    }

    public void setPackageattribute(String packageAttribute) {
        this.packageAttribute = packageAttribute;
    }
    public float getPublicattribute() {
        return publicAttribute;
    }

    public void setPublicattribute(float publicAttribute) {
        this.publicAttribute = publicAttribute;
    }
    public String getProtectedattribute() {
        return protectedAttribute;
    }

    public void setProtectedattribute(String protectedAttribute) {
        this.protectedAttribute = protectedAttribute;
    }


}