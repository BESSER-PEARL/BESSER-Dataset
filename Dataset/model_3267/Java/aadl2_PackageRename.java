





import java.util.List;
import java.util.ArrayList;

public class aadl2_PackageRename extends NamedElement {

    private String renameAll;



    public aadl2_PackageRename(
        String renameAll    ) {
        super(
        );
        this.renameAll = renameAll;
    }


    public String getRenameall() {
        return renameAll;
    }

    public void setRenameall(String renameAll) {
        this.renameAll = renameAll;
    }


}