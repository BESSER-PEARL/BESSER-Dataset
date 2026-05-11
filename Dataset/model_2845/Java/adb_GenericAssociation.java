





import java.util.List;
import java.util.ArrayList;

public class adb_GenericAssociation  {

    private String selectorName;





    private adb_GenericActualPart adb_genericactualpart;




    private adb_FormalPackageAssociation adb_formalpackageassociation;


    public adb_GenericAssociation(
        String selectorName    ) {
        this.selectorName = selectorName;
    }


    public String getSelectorname() {
        return selectorName;
    }

    public void setSelectorname(String selectorName) {
        this.selectorName = selectorName;
    }

    public adb_GenericActualPart getAdb_genericactualpart() {
        return adb_genericactualpart;
    }

    public void setAdb_genericactualpart(adb_GenericActualPart adb_genericactualpart) {
        this.adb_genericactualpart = adb_genericactualpart;
    }
    public adb_FormalPackageAssociation getAdb_formalpackageassociation() {
        return adb_formalpackageassociation;
    }

    public void setAdb_formalpackageassociation(adb_FormalPackageAssociation adb_formalpackageassociation) {
        this.adb_formalpackageassociation = adb_formalpackageassociation;
    }

}