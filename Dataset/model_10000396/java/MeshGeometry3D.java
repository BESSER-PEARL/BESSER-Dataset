





import java.util.List;
import java.util.ArrayList;

public class MeshGeometry3D  {

    private String protectedAttribute;
    private None publicAttribute;
    private String packageAttribute;
    private int privateAttribute;



    public MeshGeometry3D(
        String protectedAttribute,        None publicAttribute,        String packageAttribute,        int privateAttribute    ) {
        this.protectedAttribute = protectedAttribute;
        this.publicAttribute = publicAttribute;
        this.packageAttribute = packageAttribute;
        this.privateAttribute = privateAttribute;
    }


    public String getProtectedattribute() {
        return protectedAttribute;
    }

    public void setProtectedattribute(String protectedAttribute) {
        this.protectedAttribute = protectedAttribute;
    }
    public None getPublicattribute() {
        return publicAttribute;
    }

    public void setPublicattribute(None publicAttribute) {
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


}