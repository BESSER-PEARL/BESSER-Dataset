





import java.util.List;
import java.util.ArrayList;

public class bpmn_BpmnDiagram extends Identifiable, ArtifactsContainer {

    private String author;
    private String title;





    private List<bpmn_Pool> bpmn_pools;




    private List<bpmn_MessagingEdge> bpmn_messagingedges;




    private bpmn_Pool bpmn_pool;




    private bpmn_MessagingEdge bpmn_messagingedge;


    public bpmn_BpmnDiagram(
        String author,        String title    ) {
        super(
        );
        this.author = author;
        this.title = title;
        this.bpmn_pools = new ArrayList<>();
        this.bpmn_messagingedges = new ArrayList<>();
    }

    public bpmn_BpmnDiagram(
        String author,        String title        ArrayList<bpmn_Pool> bpmn_pools,        ArrayList<bpmn_MessagingEdge> bpmn_messagingedges    ) {
        this.author = author;
        this.title = title;
        this.bpmn_pools = bpmn_pools;
        this.bpmn_messagingedges = bpmn_messagingedges;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<bpmn_Pool> getBpmn_pools() {
        return bpmn_pools;
    }

    public void addBpmn_pool(Bpmn_pool bpmn_pool) {
        this.bpmn_pools.add(bpmn_pool);
    }
    public List<bpmn_MessagingEdge> getBpmn_messagingedges() {
        return bpmn_messagingedges;
    }

    public void addBpmn_messagingedge(Bpmn_messagingedge bpmn_messagingedge) {
        this.bpmn_messagingedges.add(bpmn_messagingedge);
    }
    public bpmn_Pool getBpmn_pool() {
        return bpmn_pool;
    }

    public void setBpmn_pool(bpmn_Pool bpmn_pool) {
        this.bpmn_pool = bpmn_pool;
    }
    public bpmn_MessagingEdge getBpmn_messagingedge() {
        return bpmn_messagingedge;
    }

    public void setBpmn_messagingedge(bpmn_MessagingEdge bpmn_messagingedge) {
        this.bpmn_messagingedge = bpmn_messagingedge;
    }

}