





import java.util.List;
import java.util.ArrayList;

public class aadl2_PackageRename extends NamedElement {

    private String renameAll;





    private aadl2_AadlPackage aadl2_aadlpackage;


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

    public aadl2_AadlPackage getAadl2_aadlpackage() {
        return aadl2_aadlpackage;
    }

    public void setAadl2_aadlpackage(aadl2_AadlPackage aadl2_aadlpackage) {
        this.aadl2_aadlpackage = aadl2_aadlpackage;
    }

}