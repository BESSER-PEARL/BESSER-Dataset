





import java.util.List;
import java.util.ArrayList;

public class adb_FormalPackageActualPart  {

    private boolean box;





    private adb_GenericActualPart adb_genericactualpart;




    private adb_FormalPackageDeclaration adb_formalpackagedeclaration;


    public adb_FormalPackageActualPart(
        boolean box    ) {
        this.box = box;
    }


    public boolean getBox() {
        return box;
    }

    public void setBox(boolean box) {
        this.box = box;
    }

    public adb_GenericActualPart getAdb_genericactualpart() {
        return adb_genericactualpart;
    }

    public void setAdb_genericactualpart(adb_GenericActualPart adb_genericactualpart) {
        this.adb_genericactualpart = adb_genericactualpart;
    }
    public adb_FormalPackageDeclaration getAdb_formalpackagedeclaration() {
        return adb_formalpackagedeclaration;
    }

    public void setAdb_formalpackagedeclaration(adb_FormalPackageDeclaration adb_formalpackagedeclaration) {
        this.adb_formalpackagedeclaration = adb_formalpackagedeclaration;
    }

}