





import java.util.List;
import java.util.ArrayList;

public class adb_PrivateTypeDeclaration extends NewTypeDeclaration {

    private boolean limited;
    private boolean abstract;
    private boolean tagged;





    private adb_DiscriminantPart adb_discriminantpart;


    public adb_PrivateTypeDeclaration(
        boolean limited,        boolean abstract,        boolean tagged    ) {
        super(
        );
        this.limited = limited;
        this.abstract = abstract;
        this.tagged = tagged;
    }


    public boolean getLimited() {
        return limited;
    }

    public void setLimited(boolean limited) {
        this.limited = limited;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getTagged() {
        return tagged;
    }

    public void setTagged(boolean tagged) {
        this.tagged = tagged;
    }

    public adb_DiscriminantPart getAdb_discriminantpart() {
        return adb_discriminantpart;
    }

    public void setAdb_discriminantpart(adb_DiscriminantPart adb_discriminantpart) {
        this.adb_discriminantpart = adb_discriminantpart;
    }

}