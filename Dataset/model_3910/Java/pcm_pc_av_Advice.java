





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_Advice  {






    private List<pcm_pc_av_EObject> pcm_pc_av_eobjects;


    public pcm_pc_av_Advice(
    ) {
        this.pcm_pc_av_eobjects = new ArrayList<>();
    }

    public pcm_pc_av_Advice(
        ArrayList<pcm_pc_av_EObject> pcm_pc_av_eobjects    ) {
        this.pcm_pc_av_eobjects = pcm_pc_av_eobjects;
    }


    public List<pcm_pc_av_EObject> getPcm_pc_av_eobjects() {
        return pcm_pc_av_eobjects;
    }

    public void addPcm_pc_av_eobject(Pcm_pc_av_eobject pcm_pc_av_eobject) {
        this.pcm_pc_av_eobjects.add(pcm_pc_av_eobject);
    }

}