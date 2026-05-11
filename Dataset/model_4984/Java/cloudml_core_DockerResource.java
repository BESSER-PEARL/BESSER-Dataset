





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_DockerResource extends Resource {

    private String dockerFilePath;
    private String image;



    public cloudml_core_DockerResource(
        String dockerFilePath,        String image    ) {
        super(
        );
        this.dockerFilePath = dockerFilePath;
        this.image = image;
    }


    public String getDockerfilepath() {
        return dockerFilePath;
    }

    public void setDockerfilepath(String dockerFilePath) {
        this.dockerFilePath = dockerFilePath;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }


}