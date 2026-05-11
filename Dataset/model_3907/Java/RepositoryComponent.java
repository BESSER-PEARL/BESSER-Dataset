





import java.util.List;
import java.util.ArrayList;

public class RepositoryComponent  {






    private pcm_composition_AssemblyContext pcm_composition_assemblycontext;




    private pcm_repository_Repository pcm_repository_repository;


    public RepositoryComponent(
    ) {
    }



    public pcm_composition_AssemblyContext getPcm_composition_assemblycontext() {
        return pcm_composition_assemblycontext;
    }

    public void setPcm_composition_assemblycontext(pcm_composition_AssemblyContext pcm_composition_assemblycontext) {
        this.pcm_composition_assemblycontext = pcm_composition_assemblycontext;
    }
    public pcm_repository_Repository getPcm_repository_repository() {
        return pcm_repository_repository;
    }

    public void setPcm_repository_repository(pcm_repository_Repository pcm_repository_repository) {
        this.pcm_repository_repository = pcm_repository_repository;
    }

}