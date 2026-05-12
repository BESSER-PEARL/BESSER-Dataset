





import java.util.List;
import java.util.ArrayList;

public class User  {

    private float publicAttribute;
    private int privateAttribute;
    private String protectedAttribute;
    private String packageAttribute;



    public User(
        float publicAttribute,        int privateAttribute,        String protectedAttribute,        String packageAttribute    ) {
        this.publicAttribute = publicAttribute;
        this.privateAttribute = privateAttribute;
        this.protectedAttribute = protectedAttribute;
        this.packageAttribute = packageAttribute;
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


}