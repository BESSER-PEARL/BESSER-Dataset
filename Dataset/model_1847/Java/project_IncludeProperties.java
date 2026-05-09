





import java.util.List;
import java.util.ArrayList;

public class project_IncludeProperties extends Property {

    private String importURI;



    public project_IncludeProperties(
        String importURI    ) {
        super(
        );
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }


}