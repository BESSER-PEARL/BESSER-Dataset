





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_ImportArtifact  {

    private String path;





    private DiagonosticModel_TestSpecification diagonosticmodel_testspecification;


    public DiagonosticModel_ImportArtifact(
        String path    ) {
        this.path = path;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public DiagonosticModel_TestSpecification getDiagonosticmodel_testspecification() {
        return diagonosticmodel_testspecification;
    }

    public void setDiagonosticmodel_testspecification(DiagonosticModel_TestSpecification diagonosticmodel_testspecification) {
        this.diagonosticmodel_testspecification = diagonosticmodel_testspecification;
    }

}