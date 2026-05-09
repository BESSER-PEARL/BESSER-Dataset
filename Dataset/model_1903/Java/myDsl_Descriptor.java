





import java.util.List;
import java.util.ArrayList;

public class myDsl_Descriptor  {

    private String path;
    private String name;





    private myDsl_Subproject mydsl_subproject;


    public myDsl_Descriptor(
        String path,        String name    ) {
        this.path = path;
        this.name = name;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Subproject getMydsl_subproject() {
        return mydsl_subproject;
    }

    public void setMydsl_subproject(myDsl_Subproject mydsl_subproject) {
        this.mydsl_subproject = mydsl_subproject;
    }

}