





import java.util.List;
import java.util.ArrayList;

public class model_Ozobot extends NamedElement {






    private List<model_OzobotProgram> model_ozobotprograms;


    public model_Ozobot(
    ) {
        super(
        );
        this.model_ozobotprograms = new ArrayList<>();
    }

    public model_Ozobot(
        ArrayList<model_OzobotProgram> model_ozobotprograms    ) {
        this.model_ozobotprograms = model_ozobotprograms;
    }


    public List<model_OzobotProgram> getModel_ozobotprograms() {
        return model_ozobotprograms;
    }

    public void addModel_ozobotprogram(Model_ozobotprogram model_ozobotprogram) {
        this.model_ozobotprograms.add(model_ozobotprogram);
    }

}