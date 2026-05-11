





import java.util.List;
import java.util.ArrayList;

public class mindmap_MindMap  {

    private String title;





    private mindmap_CentralTopic mindmap_centraltopic;


    public mindmap_MindMap(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public mindmap_CentralTopic getMindmap_centraltopic() {
        return mindmap_centraltopic;
    }

    public void setMindmap_centraltopic(mindmap_CentralTopic mindmap_centraltopic) {
        this.mindmap_centraltopic = mindmap_centraltopic;
    }

}