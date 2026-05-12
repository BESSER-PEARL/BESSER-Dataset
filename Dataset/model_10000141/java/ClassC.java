





import java.util.List;
import java.util.ArrayList;

public class ClassC  {

    private String packageAttribute;
    private String protectedAttribute;
    private int privateAttribute;
    private float publicAttribute;



    public ClassC(
        String packageAttribute,        String protectedAttribute,        int privateAttribute,        float publicAttribute    ) {
        this.packageAttribute = packageAttribute;
        this.protectedAttribute = protectedAttribute;
        this.privateAttribute = privateAttribute;
        this.publicAttribute = publicAttribute;
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
    public int getPrivateattribute() {
        return privateAttribute;
    }

    public void setPrivateattribute(int privateAttribute) {
        this.privateAttribute = privateAttribute;
    }
    public float getPublicattribute() {
        return publicAttribute;
    }

    public void setPublicattribute(float publicAttribute) {
        this.publicAttribute = publicAttribute;
    }


}