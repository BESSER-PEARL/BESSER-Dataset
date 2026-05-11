





import java.util.List;
import java.util.ArrayList;

public class adb_FormalPart  {






    private adb_AccessToSubprogramDefinition adb_accesstosubprogramdefinition;




    private adb_ProcedureSpecification adb_procedurespecification;




    private adb_EntryDeclaration adb_entrydeclaration;




    private adb_ParameterAndResultProfile adb_parameterandresultprofile;




    private List<adb_ParameterSpecification> adb_parameterspecifications;


    public adb_FormalPart(
    ) {
        this.adb_parameterspecifications = new ArrayList<>();
    }

    public adb_FormalPart(
        ArrayList<adb_ParameterSpecification> adb_parameterspecifications    ) {
        this.adb_parameterspecifications = adb_parameterspecifications;
    }


    public adb_AccessToSubprogramDefinition getAdb_accesstosubprogramdefinition() {
        return adb_accesstosubprogramdefinition;
    }

    public void setAdb_accesstosubprogramdefinition(adb_AccessToSubprogramDefinition adb_accesstosubprogramdefinition) {
        this.adb_accesstosubprogramdefinition = adb_accesstosubprogramdefinition;
    }
    public adb_ProcedureSpecification getAdb_procedurespecification() {
        return adb_procedurespecification;
    }

    public void setAdb_procedurespecification(adb_ProcedureSpecification adb_procedurespecification) {
        this.adb_procedurespecification = adb_procedurespecification;
    }
    public adb_EntryDeclaration getAdb_entrydeclaration() {
        return adb_entrydeclaration;
    }

    public void setAdb_entrydeclaration(adb_EntryDeclaration adb_entrydeclaration) {
        this.adb_entrydeclaration = adb_entrydeclaration;
    }
    public adb_ParameterAndResultProfile getAdb_parameterandresultprofile() {
        return adb_parameterandresultprofile;
    }

    public void setAdb_parameterandresultprofile(adb_ParameterAndResultProfile adb_parameterandresultprofile) {
        this.adb_parameterandresultprofile = adb_parameterandresultprofile;
    }
    public List<adb_ParameterSpecification> getAdb_parameterspecifications() {
        return adb_parameterspecifications;
    }

    public void addAdb_parameterspecification(Adb_parameterspecification adb_parameterspecification) {
        this.adb_parameterspecifications.add(adb_parameterspecification);
    }

}