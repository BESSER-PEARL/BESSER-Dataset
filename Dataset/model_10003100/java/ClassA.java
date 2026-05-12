





import java.util.List;
import java.util.ArrayList;

public class ClassA  {

    private float publicAttribute;
    private String protectedAttribute;
    private String packageAttribute;
    private int privateAttribute;



    public ClassA(
        float publicAttribute,        String protectedAttribute,        String packageAttribute,        int privateAttribute    ) {
        this.publicAttribute = publicAttribute;
        this.protectedAttribute = protectedAttribute;
        this.packageAttribute = packageAttribute;
        this.privateAttribute = privateAttribute;
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