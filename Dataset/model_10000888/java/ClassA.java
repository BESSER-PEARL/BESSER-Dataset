





import java.util.List;
import java.util.ArrayList;

public class ClassA  {

    private float publicAttribute;
    private String packageAttribute;
    private int privateAttribute;
    private String protectedAttribute;



    public ClassA(
        float publicAttribute,        String packageAttribute,        int privateAttribute,        String protectedAttribute    ) {
        this.publicAttribute = publicAttribute;
        this.packageAttribute = packageAttribute;
        this.privateAttribute = privateAttribute;
        this.protectedAttribute = protectedAttribute;
    }


    public float getPublicattribute() {
        return publicAttribute;
    }

    public void setPublicattribute(float publicAttribute) {
        this.publicAttribute = publicAttribute;
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
    public String getProtectedattribute() {
        return protectedAttribute;
    }

    public void setProtectedattribute(String protectedAttribute) {
        this.protectedAttribute = protectedAttribute;
    }


}