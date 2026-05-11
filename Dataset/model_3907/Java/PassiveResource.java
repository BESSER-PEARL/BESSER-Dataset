





import java.util.List;
import java.util.ArrayList;

public class PassiveResource  {






    private pcm_seff_ReleaseAction pcm_seff_releaseaction;




    private pcm_seff_AcquireAction pcm_seff_acquireaction;




    private pcm_repository_BasicComponent pcm_repository_basiccomponent;


    public PassiveResource(
    ) {
    }



    public pcm_seff_ReleaseAction getPcm_seff_releaseaction() {
        return pcm_seff_releaseaction;
    }

    public void setPcm_seff_releaseaction(pcm_seff_ReleaseAction pcm_seff_releaseaction) {
        this.pcm_seff_releaseaction = pcm_seff_releaseaction;
    }
    public pcm_seff_AcquireAction getPcm_seff_acquireaction() {
        return pcm_seff_acquireaction;
    }

    public void setPcm_seff_acquireaction(pcm_seff_AcquireAction pcm_seff_acquireaction) {
        this.pcm_seff_acquireaction = pcm_seff_acquireaction;
    }
    public pcm_repository_BasicComponent getPcm_repository_basiccomponent() {
        return pcm_repository_basiccomponent;
    }

    public void setPcm_repository_basiccomponent(pcm_repository_BasicComponent pcm_repository_basiccomponent) {
        this.pcm_repository_basiccomponent = pcm_repository_basiccomponent;
    }

}