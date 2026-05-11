





import java.util.List;
import java.util.ArrayList;

public class mindmap_Topic  {

    private int marker;
    private String name;



    public mindmap_Topic(
        int marker,        String name    ) {
        this.marker = marker;
        this.name = name;
    }


    public int getMarker() {
        return marker;
    }

    public void setMarker(int marker) {
        this.marker = marker;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}