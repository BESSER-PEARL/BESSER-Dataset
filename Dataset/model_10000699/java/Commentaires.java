





import java.util.List;
import java.util.ArrayList;

public class Commentaires  {

    private String protectedAttribute;
    private float idComm;
    private int privateAttribute;
    private String packageAttribute;



    public Commentaires(
        String protectedAttribute,        float idComm,        int privateAttribute,        String packageAttribute    ) {
        this.protectedAttribute = protectedAttribute;
        this.idComm = idComm;
        this.privateAttribute = privateAttribute;
        this.packageAttribute = packageAttribute;
    }


    public String getProtectedattribute() {
        return protectedAttribute;
    }

    public void setProtectedattribute(String protectedAttribute) {
        this.protectedAttribute = protectedAttribute;
    }
    public float getIdcomm() {
        return idComm;
    }

    public void setIdcomm(float idComm) {
        this.idComm = idComm;
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