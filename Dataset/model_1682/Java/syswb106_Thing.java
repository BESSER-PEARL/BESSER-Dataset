





import java.util.List;
import java.util.ArrayList;

public class syswb106_Thing  {

    private int id;





    private List<syswb106_RelatedTo> syswb106_relatedtos;




    private syswb106_RelatedTo syswb106_relatedto;




    private syswb106_Workbench syswb106_workbench;




    private syswb106_RelatedTo syswb106_relatedto;




    private syswb106_Thoughts syswb106_thoughts;


    public syswb106_Thing(
        int id    ) {
        this.id = id;
        this.syswb106_relatedtos = new ArrayList<>();
    }

    public syswb106_Thing(
        int id        ArrayList<syswb106_RelatedTo> syswb106_relatedtos    ) {
        this.id = id;
        this.syswb106_relatedtos = syswb106_relatedtos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<syswb106_RelatedTo> getSyswb106_relatedtos() {
        return syswb106_relatedtos;
    }

    public void addSyswb106_relatedto(Syswb106_relatedto syswb106_relatedto) {
        this.syswb106_relatedtos.add(syswb106_relatedto);
    }
    public syswb106_RelatedTo getSyswb106_relatedto() {
        return syswb106_relatedto;
    }

    public void setSyswb106_relatedto(syswb106_RelatedTo syswb106_relatedto) {
        this.syswb106_relatedto = syswb106_relatedto;
    }
    public syswb106_Workbench getSyswb106_workbench() {
        return syswb106_workbench;
    }

    public void setSyswb106_workbench(syswb106_Workbench syswb106_workbench) {
        this.syswb106_workbench = syswb106_workbench;
    }
    public syswb106_RelatedTo getSyswb106_relatedto() {
        return syswb106_relatedto;
    }

    public void setSyswb106_relatedto(syswb106_RelatedTo syswb106_relatedto) {
        this.syswb106_relatedto = syswb106_relatedto;
    }
    public syswb106_Thoughts getSyswb106_thoughts() {
        return syswb106_thoughts;
    }

    public void setSyswb106_thoughts(syswb106_Thoughts syswb106_thoughts) {
        this.syswb106_thoughts = syswb106_thoughts;
    }

}