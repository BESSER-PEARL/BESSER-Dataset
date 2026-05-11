





import java.util.List;
import java.util.ArrayList;

public class adb_PrivateExtensionDeclaration extends NewTypeDeclaration {

    private boolean abstract;
    private boolean synchronized;
    private boolean limited;





    private adb_DiscriminantPart adb_discriminantpart;


    public adb_PrivateExtensionDeclaration(
        boolean abstract,        boolean synchronized,        boolean limited    ) {
        super(
        );
        this.abstract = abstract;
        this.synchronized = synchronized;
        this.limited = limited;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public boolean getLimited() {
        return limited;
    }

    public void setLimited(boolean limited) {
        this.limited = limited;
    }

    public adb_DiscriminantPart getAdb_discriminantpart() {
        return adb_discriminantpart;
    }

    public void setAdb_discriminantpart(adb_DiscriminantPart adb_discriminantpart) {
        this.adb_discriminantpart = adb_discriminantpart;
    }

}