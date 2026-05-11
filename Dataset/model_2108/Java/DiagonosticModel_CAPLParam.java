





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_CAPLParam  {

    private String name;
    private String type;
    private String value;





    private DiagonosticModel_CAPLTestCase diagonosticmodel_capltestcase;




    private DiagonosticModel_CAPLTestStep diagonosticmodel_caplteststep;


    public DiagonosticModel_CAPLParam(
        String name,        String type,        String value    ) {
        this.name = name;
        this.type = type;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public DiagonosticModel_CAPLTestCase getDiagonosticmodel_capltestcase() {
        return diagonosticmodel_capltestcase;
    }

    public void setDiagonosticmodel_capltestcase(DiagonosticModel_CAPLTestCase diagonosticmodel_capltestcase) {
        this.diagonosticmodel_capltestcase = diagonosticmodel_capltestcase;
    }
    public DiagonosticModel_CAPLTestStep getDiagonosticmodel_caplteststep() {
        return diagonosticmodel_caplteststep;
    }

    public void setDiagonosticmodel_caplteststep(DiagonosticModel_CAPLTestStep diagonosticmodel_caplteststep) {
        this.diagonosticmodel_caplteststep = diagonosticmodel_caplteststep;
    }

}