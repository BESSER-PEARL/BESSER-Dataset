





import java.util.List;
import java.util.ArrayList;

public class dbrouting_DocumentRoot  {

    private String mixed;





    private List<dbrouting_Executor> dbrouting_executors;


    public dbrouting_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.dbrouting_executors = new ArrayList<>();
    }

    public dbrouting_DocumentRoot(
        String mixed        ArrayList<dbrouting_Executor> dbrouting_executors    ) {
        this.mixed = mixed;
        this.dbrouting_executors = dbrouting_executors;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<dbrouting_Executor> getDbrouting_executors() {
        return dbrouting_executors;
    }

    public void addDbrouting_executor(Dbrouting_executor dbrouting_executor) {
        this.dbrouting_executors.add(dbrouting_executor);
    }

}