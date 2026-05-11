





import java.util.List;
import java.util.ArrayList;

public class camel_Model  {

    private String importURI;
    private String name;



    public camel_Model(
        String importURI,        String name    ) {
        this.importURI = importURI;
        this.name = name;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}