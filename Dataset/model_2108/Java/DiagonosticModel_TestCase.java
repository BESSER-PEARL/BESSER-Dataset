





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_TestCase  {

    private String id;
    private String description;
    private String requirementID;
    private boolean skip;
    private String name;
    private String executionStatus;





    private List<DiagonosticModel_Variant> diagonosticmodel_variants;




    private DiagonosticModel_TestGroup diagonosticmodel_testgroup;


    public DiagonosticModel_TestCase(
        String id,        String description,        String requirementID,        boolean skip,        String name,        String executionStatus    ) {
        this.id = id;
        this.description = description;
        this.requirementID = requirementID;
        this.skip = skip;
        this.name = name;
        this.executionStatus = executionStatus;
        this.diagonosticmodel_variants = new ArrayList<>();
    }

    public DiagonosticModel_TestCase(
        String id,        String description,        String requirementID,        boolean skip,        String name,        String executionStatus        ArrayList<DiagonosticModel_Variant> diagonosticmodel_variants    ) {
        this.id = id;
        this.description = description;
        this.requirementID = requirementID;
        this.skip = skip;
        this.name = name;
        this.executionStatus = executionStatus;
        this.diagonosticmodel_variants = diagonosticmodel_variants;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getRequirementid() {
        return requirementID;
    }

    public void setRequirementid(String requirementID) {
        this.requirementID = requirementID;
    }
    public boolean getSkip() {
        return skip;
    }

    public void setSkip(boolean skip) {
        this.skip = skip;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExecutionstatus() {
        return executionStatus;
    }

    public void setExecutionstatus(String executionStatus) {
        this.executionStatus = executionStatus;
    }

    public List<DiagonosticModel_Variant> getDiagonosticmodel_variants() {
        return diagonosticmodel_variants;
    }

    public void addDiagonosticmodel_variant(Diagonosticmodel_variant diagonosticmodel_variant) {
        this.diagonosticmodel_variants.add(diagonosticmodel_variant);
    }
    public DiagonosticModel_TestGroup getDiagonosticmodel_testgroup() {
        return diagonosticmodel_testgroup;
    }

    public void setDiagonosticmodel_testgroup(DiagonosticModel_TestGroup diagonosticmodel_testgroup) {
        this.diagonosticmodel_testgroup = diagonosticmodel_testgroup;
    }

}