





import java.util.List;
import java.util.ArrayList;

public class adb_SubprogramDeclaration extends ProtectedOperationDeclaration, BasicDeclaration, ProtectedOperationItem {

    private boolean abstract;
    private String renamedName;
    private boolean null;



    public adb_SubprogramDeclaration(
        boolean abstract,        String renamedName,        boolean null    ) {
        super(
        );
        this.abstract = abstract;
        this.renamedName = renamedName;
        this.null = null;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getRenamedname() {
        return renamedName;
    }

    public void setRenamedname(String renamedName) {
        this.renamedName = renamedName;
    }
    public boolean getNull() {
        return null;
    }

    public void setNull(boolean null) {
        this.null = null;
    }


}