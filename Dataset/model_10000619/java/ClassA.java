





import java.util.List;
import java.util.ArrayList;

public class ClassA  {

    private String packageAttribute;
    private String protectedAttribute;
    private float publicAttribute;
    private int privateAttribute;



    public ClassA(
        String packageAttribute,        String protectedAttribute,        float publicAttribute,        int privateAttribute    ) {
        this.packageAttribute = packageAttribute;
        this.protectedAttribute = protectedAttribute;
        this.publicAttribute = publicAttribute;
        this.privateAttribute = privateAttribute;
    }


    public String getPackageattribute() {
        return packageAttribute;
    }

    public void setPackageattribute(String packageAttribute) {
        this.packageAttribute = packageAttribute;
    }
    public String getProtectedattribute() {
        return protectedAttribute;
    }

    public void setProtectedattribute(String protectedAttribute) {
        this.protectedAttribute = protectedAttribute;
    }
    public float getPublicattribute() {
        return publicAttribute;
    }

    public void setPublicattribute(float publicAttribute) {
        this.publicAttribute = publicAttribute;
    }
    public int getPrivateattribute() {
        return privateAttribute;
    }

    public void setPrivateattribute(int privateAttribute) {
        this.privateAttribute = privateAttribute;
    }


}