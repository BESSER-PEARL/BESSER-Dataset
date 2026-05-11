





import java.util.List;
import java.util.ArrayList;

public class fiacre_State extends EModelElement {

    private String ID;





    private fiacre_Process fiacre_process;


    public fiacre_State(
        String ID    ) {
        super(
        );
        this.ID = ID;
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

}