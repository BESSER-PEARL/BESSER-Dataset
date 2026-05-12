





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_Export  {

    private String name;





    private sourcecleaner_Manifest sourcecleaner_manifest;


    public sourcecleaner_Export(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sourcecleaner_Manifest getSourcecleaner_manifest() {
        return sourcecleaner_manifest;
    }

    public void setSourcecleaner_manifest(sourcecleaner_Manifest sourcecleaner_manifest) {
        this.sourcecleaner_manifest = sourcecleaner_manifest;
    }

}