





import java.util.List;
import java.util.ArrayList;

public class gastm_SourceFile extends GASTMSourceObject {

    private String pathName;



    public gastm_SourceFile(
        String pathName    ) {
        super(
        );
        this.pathName = pathName;
    }


    public String getPathname() {
        return pathName;
    }

    public void setPathname(String pathName) {
        this.pathName = pathName;
    }


}