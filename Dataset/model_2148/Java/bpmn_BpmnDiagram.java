





import java.util.List;
import java.util.ArrayList;

public class bpmn_BpmnDiagram extends ArtifactsContainer, Identifiable {

    private String title;
    private String author;





    private bpmn_Pool bpmn_pool;




    private List<bpmn_Pool> bpmn_pools;


    public bpmn_BpmnDiagram(
        String title,        String author    ) {
        super(
        );
        this.title = title;
        this.author = author;
        this.bpmn_pools = new ArrayList<>();
    }

    public bpmn_BpmnDiagram(
        String title,        String author        ArrayList<bpmn_Pool> bpmn_pools    ) {
        this.title = title;
        this.author = author;
        this.bpmn_pools = bpmn_pools;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public bpmn_Pool getBpmn_pool() {
        return bpmn_pool;
    }

    public void setBpmn_pool(bpmn_Pool bpmn_pool) {
        this.bpmn_pool = bpmn_pool;
    }
    public List<bpmn_Pool> getBpmn_pools() {
        return bpmn_pools;
    }

    public void addBpmn_pool(Bpmn_pool bpmn_pool) {
        this.bpmn_pools.add(bpmn_pool);
    }

}