





import java.util.List;
import java.util.ArrayList;

public class ValidationModel_UnitTest  {

    private String name;
    private String id;
    private boolean isTested;





    private ValidationModel_TestContainer validationmodel_testcontainer;


    public ValidationModel_UnitTest(
        String name,        String id,        boolean isTested    ) {
        this.name = name;
        this.id = id;
        this.isTested = isTested;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getIstested() {
        return isTested;
    }

    public void setIstested(boolean isTested) {
        this.isTested = isTested;
    }

    public ValidationModel_TestContainer getValidationmodel_testcontainer() {
        return validationmodel_testcontainer;
    }

    public void setValidationmodel_testcontainer(ValidationModel_TestContainer validationmodel_testcontainer) {
        this.validationmodel_testcontainer = validationmodel_testcontainer;
    }

}