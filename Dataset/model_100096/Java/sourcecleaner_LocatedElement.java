





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_LocatedElement  {

    private String name;
    private String absolutePath;



    public sourcecleaner_LocatedElement(
        String name,        String absolutePath    ) {
        this.name = name;
        this.absolutePath = absolutePath;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAbsolutepath() {
        return absolutePath;
    }

    public void setAbsolutepath(String absolutePath) {
        this.absolutePath = absolutePath;
    }


}