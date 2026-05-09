





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_LocatedElement  {

    private String fileObject;
    private String fileLocation;



    public atlext_ATL_LocatedElement(
        String fileObject,        String fileLocation    ) {
        this.fileObject = fileObject;
        this.fileLocation = fileLocation;
    }


    public String getFileobject() {
        return fileObject;
    }

    public void setFileobject(String fileObject) {
        this.fileObject = fileObject;
    }
    public String getFilelocation() {
        return fileLocation;
    }

    public void setFilelocation(String fileLocation) {
        this.fileLocation = fileLocation;
    }


}