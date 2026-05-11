





import java.util.List;
import java.util.ArrayList;

public class p2_Property  {

    private String value;
    private String key;





    private p2_ArtifactDescriptor p2_artifactdescriptor;


    public p2_Property(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public p2_ArtifactDescriptor getP2_artifactdescriptor() {
        return p2_artifactdescriptor;
    }

    public void setP2_artifactdescriptor(p2_ArtifactDescriptor p2_artifactdescriptor) {
        this.p2_artifactdescriptor = p2_artifactdescriptor;
    }

}