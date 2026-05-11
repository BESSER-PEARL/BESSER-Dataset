





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_Variant  {

    private String name;
    private String description;





    private DiagonosticModel_TestSpecification diagonosticmodel_testspecification;


    public DiagonosticModel_Variant(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public DiagonosticModel_TestSpecification getDiagonosticmodel_testspecification() {
        return diagonosticmodel_testspecification;
    }

    public void setDiagonosticmodel_testspecification(DiagonosticModel_TestSpecification diagonosticmodel_testspecification) {
        this.diagonosticmodel_testspecification = diagonosticmodel_testspecification;
    }

}