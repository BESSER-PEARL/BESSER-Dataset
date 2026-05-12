





import java.util.List;
import java.util.ArrayList;

public class RazredA  {

    private String packageAtribut;
    private int privateAtribut;
    private float publicAtribut;
    private String protectedAtribut;



    public RazredA(
        String packageAtribut,        int privateAtribut,        float publicAtribut,        String protectedAtribut    ) {
        this.packageAtribut = packageAtribut;
        this.privateAtribut = privateAtribut;
        this.publicAtribut = publicAtribut;
        this.protectedAtribut = protectedAtribut;
    }


    public String getPackageatribut() {
        return packageAtribut;
    }

    public void setPackageatribut(String packageAtribut) {
        this.packageAtribut = packageAtribut;
    }
    public int getPrivateatribut() {
        return privateAtribut;
    }

    public void setPrivateatribut(int privateAtribut) {
        this.privateAtribut = privateAtribut;
    }
    public float getPublicatribut() {
        return publicAtribut;
    }

    public void setPublicatribut(float publicAtribut) {
        this.publicAtribut = publicAtribut;
    }
    public String getProtectedatribut() {
        return protectedAtribut;
    }

    public void setProtectedatribut(String protectedAtribut) {
        this.protectedAtribut = protectedAtribut;
    }


}