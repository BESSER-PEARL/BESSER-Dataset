





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Control extends Element {






    private contentfwk_Process contentfwk_process;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_Process> contentfwk_processs;


    public contentfwk_Control(
    ) {
        super(
        );
        this.contentfwk_processs = new ArrayList<>();
    }

    public contentfwk_Control(
        ArrayList<contentfwk_Process> contentfwk_processs    ) {
        this.contentfwk_processs = contentfwk_processs;
    }


    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }

}