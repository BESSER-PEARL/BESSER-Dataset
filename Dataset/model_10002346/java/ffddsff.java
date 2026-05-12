





import java.util.List;
import java.util.ArrayList;

public class ffddsff  {

    private String attribute;
    private float publicAttribute;
    private String protectedAttribute;
    private String packageAttribute;
    private int privateAttribute;



    public ffddsff(
        String attribute,        float publicAttribute,        String protectedAttribute,        String packageAttribute,        int privateAttribute    ) {
        this.attribute = attribute;
        this.publicAttribute = publicAttribute;
        this.protectedAttribute = protectedAttribute;
        this.packageAttribute = packageAttribute;
        this.privateAttribute = privateAttribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
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
    public String getPackageattribute() {
        return packageAttribute;
    }

    public void setPackageattribute(String packageAttribute) {
        this.packageAttribute = packageAttribute;
    }
    public int getPrivateattribute() {
        return privateAttribute;
    }

    public void setPrivateattribute(int privateAttribute) {
        this.privateAttribute = privateAttribute;
    }


}