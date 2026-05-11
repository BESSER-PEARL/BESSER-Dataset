





import java.util.List;
import java.util.ArrayList;

public class di_View  {

    private String label;
    private String id;



    public di_View(
        String label,        String id    ) {
        this.label = label;
        this.id = id;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}