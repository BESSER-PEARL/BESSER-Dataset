





import java.util.List;
import java.util.ArrayList;

public class fiacre_Variable extends EModelElement {

    private String ID;





    private fiacre_Process fiacre_process;




    private List<fiacre_Process> fiacre_processs;


    public fiacre_Variable(
        String ID    ) {
        super(
        );
        this.ID = ID;
        this.fiacre_processs = new ArrayList<>();
    }

    public fiacre_Variable(
        String ID        ArrayList<fiacre_Process> fiacre_processs    ) {
        this.ID = ID;
        this.fiacre_processs = fiacre_processs;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public fiacre_Process getFiacre_process() {
        return fiacre_process;
    }

    public void setFiacre_process(fiacre_Process fiacre_process) {
        this.fiacre_process = fiacre_process;
    }
    public List<fiacre_Process> getFiacre_processs() {
        return fiacre_processs;
    }

    public void addFiacre_process(Fiacre_process fiacre_process) {
        this.fiacre_processs.add(fiacre_process);
    }

}