





import java.util.List;
import java.util.ArrayList;

public class limp_Import extends Declaration {

    private String importURI;



    public limp_Import(
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