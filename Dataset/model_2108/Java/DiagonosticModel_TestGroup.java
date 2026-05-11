





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_TestGroup  {

    private String description;
    private String name;





    private DiagonosticModel_TestGroup diagonosticmodel_testgroup;




    private DiagonosticModel_TestSpecification diagonosticmodel_testspecification;


    public DiagonosticModel_TestGroup(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public DiagonosticModel_TestGroup getDiagonosticmodel_testgroup() {
        return diagonosticmodel_testgroup;
    }

    public void setDiagonosticmodel_testgroup(DiagonosticModel_TestGroup diagonosticmodel_testgroup) {
        this.diagonosticmodel_testgroup = diagonosticmodel_testgroup;
    }
    public DiagonosticModel_TestSpecification getDiagonosticmodel_testspecification() {
        return diagonosticmodel_testspecification;
    }

    public void setDiagonosticmodel_testspecification(DiagonosticModel_TestSpecification diagonosticmodel_testspecification) {
        this.diagonosticmodel_testspecification = diagonosticmodel_testspecification;
    }

}