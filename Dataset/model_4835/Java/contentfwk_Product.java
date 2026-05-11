





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Product extends Element {






    private contentfwk_Process contentfwk_process;




    private List<contentfwk_Process> contentfwk_processs;


    public contentfwk_Product(
    ) {
        super(
        );
        this.contentfwk_processs = new ArrayList<>();
    }

    public contentfwk_Product(
        ArrayList<contentfwk_Process> contentfwk_processs    ) {
        this.contentfwk_processs = contentfwk_processs;
    }


    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }

}