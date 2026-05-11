





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_BlockAction extends TestStep {






    private List<DiagonosticModel_TestStep> diagonosticmodel_teststeps;


    public DiagonosticModel_BlockAction(
    ) {
        super(
        );
        this.diagonosticmodel_teststeps = new ArrayList<>();
    }

    public DiagonosticModel_BlockAction(
        ArrayList<DiagonosticModel_TestStep> diagonosticmodel_teststeps    ) {
        this.diagonosticmodel_teststeps = diagonosticmodel_teststeps;
    }


    public List<DiagonosticModel_TestStep> getDiagonosticmodel_teststeps() {
        return diagonosticmodel_teststeps;
    }

    public void addDiagonosticmodel_teststep(Diagonosticmodel_teststep diagonosticmodel_teststep) {
        this.diagonosticmodel_teststeps.add(diagonosticmodel_teststep);
    }

}