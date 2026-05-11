





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_repository_pc_Repository extends Entity {

    private String repositoryDescription;



    public pcm_pc_repository_pc_Repository(
        String repositoryDescription    ) {
        super(
        );
        this.repositoryDescription = repositoryDescription;
    }


    public String getRepositorydescription() {
        return repositoryDescription;
    }

    public void setRepositorydescription(String repositoryDescription) {
        this.repositoryDescription = repositoryDescription;
    }


}