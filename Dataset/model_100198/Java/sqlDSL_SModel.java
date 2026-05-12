





import java.util.List;
import java.util.ArrayList;

public class sqlDSL_SModel  {

    private String generatedFile;





    private List<sqlDSL_SArtifact> sqldsl_sartifacts;


    public sqlDSL_SModel(
        String generatedFile    ) {
        this.generatedFile = generatedFile;
        this.sqldsl_sartifacts = new ArrayList<>();
    }

    public sqlDSL_SModel(
        String generatedFile        ArrayList<sqlDSL_SArtifact> sqldsl_sartifacts    ) {
        this.generatedFile = generatedFile;
        this.sqldsl_sartifacts = sqldsl_sartifacts;
    }

    public String getGeneratedfile() {
        return generatedFile;
    }

    public void setGeneratedfile(String generatedFile) {
        this.generatedFile = generatedFile;
    }

    public List<sqlDSL_SArtifact> getSqldsl_sartifacts() {
        return sqldsl_sartifacts;
    }

    public void addSqldsl_sartifact(Sqldsl_sartifact sqldsl_sartifact) {
        this.sqldsl_sartifacts.add(sqldsl_sartifact);
    }

}