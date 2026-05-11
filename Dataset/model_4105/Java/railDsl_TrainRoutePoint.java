





import java.util.List;
import java.util.ArrayList;

public class railDsl_TrainRoutePoint extends TrainRouteObject {

    private int selectedInput;
    private int selectedOutput;





    private railDsl_Point raildsl_point;


    public railDsl_TrainRoutePoint(
        int selectedInput,        int selectedOutput    ) {
        super(
        );
        this.selectedInput = selectedInput;
        this.selectedOutput = selectedOutput;
    }


    public int getSelectedinput() {
        return selectedInput;
    }

    public void setSelectedinput(int selectedInput) {
        this.selectedInput = selectedInput;
    }
    public int getSelectedoutput() {
        return selectedOutput;
    }

    public void setSelectedoutput(int selectedOutput) {
        this.selectedOutput = selectedOutput;
    }

    public railDsl_Point getRaildsl_point() {
        return raildsl_point;
    }

    public void setRaildsl_point(railDsl_Point raildsl_point) {
        this.raildsl_point = raildsl_point;
    }

}