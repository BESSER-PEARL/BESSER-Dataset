





import java.util.List;
import java.util.ArrayList;

public class mindmap_CentralTopic extends Topic {






    private List<mindmap_MainTopic> mindmap_maintopics;


    public mindmap_CentralTopic(
    ) {
        super(
        );
        this.mindmap_maintopics = new ArrayList<>();
    }

    public mindmap_CentralTopic(
        ArrayList<mindmap_MainTopic> mindmap_maintopics    ) {
        this.mindmap_maintopics = mindmap_maintopics;
    }


    public List<mindmap_MainTopic> getMindmap_maintopics() {
        return mindmap_maintopics;
    }

    public void addMindmap_maintopic(Mindmap_maintopic mindmap_maintopic) {
        this.mindmap_maintopics.add(mindmap_maintopic);
    }

}