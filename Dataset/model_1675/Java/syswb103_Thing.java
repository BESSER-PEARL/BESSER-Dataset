





import java.util.List;
import java.util.ArrayList;

public class syswb103_Thing extends NamedElement {

    private int id;





    private List<syswb103_RelatedTo> syswb103_relatedtos;




    private syswb103_RelatedTo syswb103_relatedto;




    private syswb103_RelatedTo syswb103_relatedto;




    private syswb103_Workbench syswb103_workbench;


    public syswb103_Thing(
        int id    ) {
        super(
        );
        this.id = id;
        this.syswb103_relatedtos = new ArrayList<>();
    }

    public syswb103_Thing(
        int id        ArrayList<syswb103_RelatedTo> syswb103_relatedtos    ) {
        this.id = id;
        this.syswb103_relatedtos = syswb103_relatedtos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<syswb103_RelatedTo> getSyswb103_relatedtos() {
        return syswb103_relatedtos;
    }

    public void addSyswb103_relatedto(Syswb103_relatedto syswb103_relatedto) {
        this.syswb103_relatedtos.add(syswb103_relatedto);
    }
    public syswb103_RelatedTo getSyswb103_relatedto() {
        return syswb103_relatedto;
    }

    public void setSyswb103_relatedto(syswb103_RelatedTo syswb103_relatedto) {
        this.syswb103_relatedto = syswb103_relatedto;
    }
    public syswb103_RelatedTo getSyswb103_relatedto() {
        return syswb103_relatedto;
    }

    public void setSyswb103_relatedto(syswb103_RelatedTo syswb103_relatedto) {
        this.syswb103_relatedto = syswb103_relatedto;
    }
    public syswb103_Workbench getSyswb103_workbench() {
        return syswb103_workbench;
    }

    public void setSyswb103_workbench(syswb103_Workbench syswb103_workbench) {
        this.syswb103_workbench = syswb103_workbench;
    }

}