





import java.util.List;
import java.util.ArrayList;

public class Repository  {






    private pcm_av_pc_repository_av_pc_Interface pcm_av_pc_repository_av_pc_interface;




    private pcm_av_pc_reliability_av_pc_FailureType pcm_av_pc_reliability_av_pc_failuretype;




    private pcm_av_pc_repository_av_pc_RepositoryComponent pcm_av_pc_repository_av_pc_repositorycomponent;


    public Repository(
    ) {
    }



    public pcm_av_pc_repository_av_pc_Interface getPcm_av_pc_repository_av_pc_interface() {
        return pcm_av_pc_repository_av_pc_interface;
    }

    public void setPcm_av_pc_repository_av_pc_interface(pcm_av_pc_repository_av_pc_Interface pcm_av_pc_repository_av_pc_interface) {
        this.pcm_av_pc_repository_av_pc_interface = pcm_av_pc_repository_av_pc_interface;
    }
    public pcm_av_pc_reliability_av_pc_FailureType getPcm_av_pc_reliability_av_pc_failuretype() {
        return pcm_av_pc_reliability_av_pc_failuretype;
    }

    public void setPcm_av_pc_reliability_av_pc_failuretype(pcm_av_pc_reliability_av_pc_FailureType pcm_av_pc_reliability_av_pc_failuretype) {
        this.pcm_av_pc_reliability_av_pc_failuretype = pcm_av_pc_reliability_av_pc_failuretype;
    }
    public pcm_av_pc_repository_av_pc_RepositoryComponent getPcm_av_pc_repository_av_pc_repositorycomponent() {
        return pcm_av_pc_repository_av_pc_repositorycomponent;
    }

    public void setPcm_av_pc_repository_av_pc_repositorycomponent(pcm_av_pc_repository_av_pc_RepositoryComponent pcm_av_pc_repository_av_pc_repositorycomponent) {
        this.pcm_av_pc_repository_av_pc_repositorycomponent = pcm_av_pc_repository_av_pc_repositorycomponent;
    }

}