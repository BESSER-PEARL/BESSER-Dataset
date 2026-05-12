





import java.util.List;
import java.util.ArrayList;

public class builds_Artifact extends BuildElement {

    private String relativePath;



    public builds_Artifact(
        String relativePath    ) {
        super(
        );
        this.relativePath = relativePath;
    }


    public String getRelativepath() {
        return relativePath;
    }

    public void setRelativepath(String relativePath) {
        this.relativePath = relativePath;
    }


}