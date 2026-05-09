





import java.util.List;
import java.util.ArrayList;

public class sam_Model  {






    private sam_ModelContent sam_modelcontent;




    private sam_FlowGroup sam_flowgroup;




    private List<sam_FlowGroup> sam_flowgroups;




    private sam_ModelContent sam_modelcontent;


    public sam_Model(
    ) {
        this.sam_flowgroups = new ArrayList<>();
    }

    public sam_Model(
        ArrayList<sam_FlowGroup> sam_flowgroups    ) {
        this.sam_flowgroups = sam_flowgroups;
    }


    public sam_ModelContent getSam_modelcontent() {
        return sam_modelcontent;
    }

    public void setSam_modelcontent(sam_ModelContent sam_modelcontent) {
        this.sam_modelcontent = sam_modelcontent;
    }
    public sam_FlowGroup getSam_flowgroup() {
        return sam_flowgroup;
    }

    public void setSam_flowgroup(sam_FlowGroup sam_flowgroup) {
        this.sam_flowgroup = sam_flowgroup;
    }
    public List<sam_FlowGroup> getSam_flowgroups() {
        return sam_flowgroups;
    }

    public void addSam_flowgroup(Sam_flowgroup sam_flowgroup) {
        this.sam_flowgroups.add(sam_flowgroup);
    }
    public sam_ModelContent getSam_modelcontent() {
        return sam_modelcontent;
    }

    public void setSam_modelcontent(sam_ModelContent sam_modelcontent) {
        this.sam_modelcontent = sam_modelcontent;
    }

}