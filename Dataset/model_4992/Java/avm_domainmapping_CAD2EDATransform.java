





import java.util.List;
import java.util.ArrayList;

public class avm_domainmapping_CAD2EDATransform extends DomainMapping {

    private String TranslationX;
    private String TranslationZ;
    private String TranslationY;
    private String ScaleY;
    private String RotationY;
    private String ScaleX;
    private String RotationZ;
    private String RotationX;
    private String ScaleZ;



    public avm_domainmapping_CAD2EDATransform(
        String TranslationX,        String TranslationZ,        String TranslationY,        String ScaleY,        String RotationY,        String ScaleX,        String RotationZ,        String RotationX,        String ScaleZ    ) {
        super(
        );
        this.TranslationX = TranslationX;
        this.TranslationZ = TranslationZ;
        this.TranslationY = TranslationY;
        this.ScaleY = ScaleY;
        this.RotationY = RotationY;
        this.ScaleX = ScaleX;
        this.RotationZ = RotationZ;
        this.RotationX = RotationX;
        this.ScaleZ = ScaleZ;
    }


    public String getTranslationx() {
        return TranslationX;
    }

    public void setTranslationx(String TranslationX) {
        this.TranslationX = TranslationX;
    }
    public String getTranslationz() {
        return TranslationZ;
    }

    public void setTranslationz(String TranslationZ) {
        this.TranslationZ = TranslationZ;
    }
    public String getTranslationy() {
        return TranslationY;
    }

    public void setTranslationy(String TranslationY) {
        this.TranslationY = TranslationY;
    }
    public String getScaley() {
        return ScaleY;
    }

    public void setScaley(String ScaleY) {
        this.ScaleY = ScaleY;
    }
    public String getRotationy() {
        return RotationY;
    }

    public void setRotationy(String RotationY) {
        this.RotationY = RotationY;
    }
    public String getScalex() {
        return ScaleX;
    }

    public void setScalex(String ScaleX) {
        this.ScaleX = ScaleX;
    }
    public String getRotationz() {
        return RotationZ;
    }

    public void setRotationz(String RotationZ) {
        this.RotationZ = RotationZ;
    }
    public String getRotationx() {
        return RotationX;
    }

    public void setRotationx(String RotationX) {
        this.RotationX = RotationX;
    }
    public String getScalez() {
        return ScaleZ;
    }

    public void setScalez(String ScaleZ) {
        this.ScaleZ = ScaleZ;
    }


}