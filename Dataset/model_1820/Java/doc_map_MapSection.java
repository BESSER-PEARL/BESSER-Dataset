





import java.util.List;
import java.util.ArrayList;

public class doc_map_MapSection extends map_MapContainer, map_MapElement {

    private String title;
    private String id;



    public doc_map_MapSection(
        String title,        String id    ) {
        super(
        );
        this.title = title;
        this.id = id;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}