





import java.util.List;
import java.util.ArrayList;

public class swrtj_Import  {

    private String importURI;





    private swrtj_File swrtj_file;


    public swrtj_Import(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public swrtj_File getSwrtj_file() {
        return swrtj_file;
    }

    public void setSwrtj_file(swrtj_File swrtj_file) {
        this.swrtj_file = swrtj_file;
    }

}