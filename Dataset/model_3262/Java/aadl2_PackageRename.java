





import java.util.List;
import java.util.ArrayList;

public class aadl2_PackageRename extends NamedElement {

    private String renameAll;





    private aadl2_PackageSection aadl2_packagesection;


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

    public aadl2_PackageSection getAadl2_packagesection() {
        return aadl2_packagesection;
    }

    public void setAadl2_packagesection(aadl2_PackageSection aadl2_packagesection) {
        this.aadl2_packagesection = aadl2_packagesection;
    }

}