





import java.util.List;
import java.util.ArrayList;

public class statechart_Model  {

    private String metadata;
    private String name;
    private String description;



    public statechart_Model(
        String metadata,        String name,        String description    ) {
        this.metadata = metadata;
        this.name = name;
        this.description = description;
    }


    public String getMetadata() {
        return metadata;
    }

    public void setMetadata(String metadata) {
        this.metadata = metadata;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}