





import java.util.List;
import java.util.ArrayList;

public class ClassC  {

    private float publicAttribute;
    private String protectedAttribute;
    private int privateAttribute;
    private String packageAttribute;



    public ClassC(
        float publicAttribute,        String protectedAttribute,        int privateAttribute,        String packageAttribute    ) {
        this.publicAttribute = publicAttribute;
        this.protectedAttribute = protectedAttribute;
        this.privateAttribute = privateAttribute;
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


}