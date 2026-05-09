





import java.util.List;
import java.util.ArrayList;

public class project_Export extends Property {

    private String id;
    private String filename;



    public project_Export(
        String id,        String filename    ) {
        super(
        );
        this.id = id;
        this.filename = filename;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }


}