





import java.util.List;
import java.util.ArrayList;

public class mindmap_SubTopic extends Topic {






    private List<mindmap_SubTopic> mindmap_subtopics;




    private mindmap_MainTopic mindmap_maintopic;


    public mindmap_SubTopic(
    ) {
        super(
        );
        this.mindmap_subtopics = new ArrayList<>();
    }

    public mindmap_SubTopic(
        ArrayList<mindmap_SubTopic> mindmap_subtopics    ) {
        this.mindmap_subtopics = mindmap_subtopics;
    }


    public List<mindmap_SubTopic> getMindmap_subtopics() {
        return mindmap_subtopics;
    }

    public void addMindmap_subtopic(Mindmap_subtopic mindmap_subtopic) {
        this.mindmap_subtopics.add(mindmap_subtopic);
    }
    public mindmap_MainTopic getMindmap_maintopic() {
        return mindmap_maintopic;
    }

    public void setMindmap_maintopic(mindmap_MainTopic mindmap_maintopic) {
        this.mindmap_maintopic = mindmap_maintopic;
    }

}