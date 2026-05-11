





import java.util.List;
import java.util.ArrayList;

public class model_Ozobot extends NamedElement {

    private float xposition;
    private float orientation;
    private float yposition;





    private List<model_OzobotProgram> model_ozobotprograms;


    public model_Ozobot(
        float xposition,        float orientation,        float yposition    ) {
        super(
        );
        this.xposition = xposition;
        this.orientation = orientation;
        this.yposition = yposition;
        this.model_ozobotprograms = new ArrayList<>();
    }

    public model_Ozobot(
        float xposition,        float orientation,        float yposition        ArrayList<model_OzobotProgram> model_ozobotprograms    ) {
        this.xposition = xposition;
        this.orientation = orientation;
        this.yposition = yposition;
        this.model_ozobotprograms = model_ozobotprograms;
    }

    public float getXposition() {
        return xposition;
    }

    public void setXposition(float xposition) {
        this.xposition = xposition;
    }
    public float getOrientation() {
        return orientation;
    }

    public void setOrientation(float orientation) {
        this.orientation = orientation;
    }
    public float getYposition() {
        return yposition;
    }

    public void setYposition(float yposition) {
        this.yposition = yposition;
    }

    public List<model_OzobotProgram> getModel_ozobotprograms() {
        return model_ozobotprograms;
    }

    public void addModel_ozobotprogram(Model_ozobotprogram model_ozobotprogram) {
        this.model_ozobotprograms.add(model_ozobotprogram);
    }

}