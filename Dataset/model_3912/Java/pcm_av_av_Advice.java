





import java.util.List;
import java.util.ArrayList;

public class pcm_av_av_Advice  {






    private List<pcm_av_av_EObject> pcm_av_av_eobjects;


    public pcm_av_av_Advice(
    ) {
        this.pcm_av_av_eobjects = new ArrayList<>();
    }

    public pcm_av_av_Advice(
        ArrayList<pcm_av_av_EObject> pcm_av_av_eobjects    ) {
        this.pcm_av_av_eobjects = pcm_av_av_eobjects;
    }


    public List<pcm_av_av_EObject> getPcm_av_av_eobjects() {
        return pcm_av_av_eobjects;
    }

    public void addPcm_av_av_eobject(Pcm_av_av_eobject pcm_av_av_eobject) {
        this.pcm_av_av_eobjects.add(pcm_av_av_eobject);
    }

}