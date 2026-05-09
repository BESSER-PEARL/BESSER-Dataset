





import java.util.List;
import java.util.ArrayList;

public class doc_map_MapSection extends map_MapElement, map_MapContainer {

    private String id;
    private String title;



    public doc_map_MapSection(
        String id,        String title    ) {
        super(
        );
        this.id = id;
        this.title = title;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}