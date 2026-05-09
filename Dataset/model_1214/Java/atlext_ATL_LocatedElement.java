





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_LocatedElement  {

    private String fileLocation;
    private String fileObject;



    public atlext_ATL_LocatedElement(
        String fileLocation,        String fileObject    ) {
        this.fileLocation = fileLocation;
        this.fileObject = fileObject;
    }


    public String getFilelocation() {
        return fileLocation;
    }

    public void setFilelocation(String fileLocation) {
        this.fileLocation = fileLocation;
    }
    public String getFileobject() {
        return fileObject;
    }

    public void setFileobject(String fileObject) {
        this.fileObject = fileObject;
    }


}