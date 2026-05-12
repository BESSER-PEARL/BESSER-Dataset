





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_document_BPMHumanTaskDocument extends LuniferaDocDocument {

    private String task;



    public luniferadoc_document_BPMHumanTaskDocument(
        String task    ) {
        super(
        );
        this.task = task;
    }


    public String getTask() {
        return task;
    }

    public void setTask(String task) {
        this.task = task;
    }


}