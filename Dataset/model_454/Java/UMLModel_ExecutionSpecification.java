





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ExecutionSpecification extends InteractionFragment {

    private String start;
    private String finish;



    public UMLModel_ExecutionSpecification(
        String start,        String finish    ) {
        super(
        );
        this.start = start;
        this.finish = finish;
    }


    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getFinish() {
        return finish;
    }

    public void setFinish(String finish) {
        this.finish = finish;
    }


}