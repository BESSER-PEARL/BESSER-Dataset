





import java.util.List;
import java.util.ArrayList;

public class adb_FormalPackageAssociation  {

    private String genericFormalParameterSelectorName;





    private adb_FormalPackageActualPart adb_formalpackageactualpart;


    public adb_FormalPackageAssociation(
        String genericFormalParameterSelectorName    ) {
        this.genericFormalParameterSelectorName = genericFormalParameterSelectorName;
    }


    public String getGenericformalparameterselectorname() {
        return genericFormalParameterSelectorName;
    }

    public void setGenericformalparameterselectorname(String genericFormalParameterSelectorName) {
        this.genericFormalParameterSelectorName = genericFormalParameterSelectorName;
    }

    public adb_FormalPackageActualPart getAdb_formalpackageactualpart() {
        return adb_formalpackageactualpart;
    }

    public void setAdb_formalpackageactualpart(adb_FormalPackageActualPart adb_formalpackageactualpart) {
        this.adb_formalpackageactualpart = adb_formalpackageactualpart;
    }

}