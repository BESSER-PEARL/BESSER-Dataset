





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_Pointcut  {






    private List<pcm_pc_pc_EObject> pcm_pc_pc_eobjects;


    public pcm_pc_pc_Pointcut(
    ) {
        this.pcm_pc_pc_eobjects = new ArrayList<>();
    }

    public pcm_pc_pc_Pointcut(
        ArrayList<pcm_pc_pc_EObject> pcm_pc_pc_eobjects    ) {
        this.pcm_pc_pc_eobjects = pcm_pc_pc_eobjects;
    }


    public List<pcm_pc_pc_EObject> getPcm_pc_pc_eobjects() {
        return pcm_pc_pc_eobjects;
    }

    public void addPcm_pc_pc_eobject(Pcm_pc_pc_eobject pcm_pc_pc_eobject) {
        this.pcm_pc_pc_eobjects.add(pcm_pc_pc_eobject);
    }

}