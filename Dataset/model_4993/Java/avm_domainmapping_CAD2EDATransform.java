





import java.util.List;
import java.util.ArrayList;

public class avm_domainmapping_CAD2EDATransform extends DomainMapping {

    private String TranslationY;
    private String ScaleX;
    private String RotationX;
    private String ScaleY;
    private String TranslationX;
    private String ScaleZ;
    private String RotationZ;
    private String TranslationZ;
    private String RotationY;



    public avm_domainmapping_CAD2EDATransform(
        String TranslationY,        String ScaleX,        String RotationX,        String ScaleY,        String TranslationX,        String ScaleZ,        String RotationZ,        String TranslationZ,        String RotationY    ) {
        super(
        );
        this.TranslationY = TranslationY;
        this.ScaleX = ScaleX;
        this.RotationX = RotationX;
        this.ScaleY = ScaleY;
        this.TranslationX = TranslationX;
        this.ScaleZ = ScaleZ;
        this.RotationZ = RotationZ;
        this.TranslationZ = TranslationZ;
        this.RotationY = RotationY;
    }


    public String getTranslationy() {
        return TranslationY;
    }

    public void setTranslationy(String TranslationY) {
        this.TranslationY = TranslationY;
    }
    public String getScalex() {
        return ScaleX;
    }

    public void setScalex(String ScaleX) {
        this.ScaleX = ScaleX;
    }
    public String getRotationx() {
        return RotationX;
    }

    public void setRotationx(String RotationX) {
        this.RotationX = RotationX;
    }
    public String getScaley() {
        return ScaleY;
    }

    public void setScaley(String ScaleY) {
        this.ScaleY = ScaleY;
    }
    public String getTranslationx() {
        return TranslationX;
    }

    public void setTranslationx(String TranslationX) {
        this.TranslationX = TranslationX;
    }
    public String getScalez() {
        return ScaleZ;
    }

    public void setScalez(String ScaleZ) {
        this.ScaleZ = ScaleZ;
    }
    public String getRotationz() {
        return RotationZ;
    }

    public void setRotationz(String RotationZ) {
        this.RotationZ = RotationZ;
    }
    public String getTranslationz() {
        return TranslationZ;
    }

    public void setTranslationz(String TranslationZ) {
        this.TranslationZ = TranslationZ;
    }
    public String getRotationy() {
        return RotationY;
    }

    public void setRotationy(String RotationY) {
        this.RotationY = RotationY;
    }


}