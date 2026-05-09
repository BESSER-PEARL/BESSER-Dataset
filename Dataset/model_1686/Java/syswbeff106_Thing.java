





import java.util.List;
import java.util.ArrayList;

public class syswbeff106_Thing  {

    private int id;





    private syswbeff106_RelatedTo syswbeff106_relatedto;




    private List<syswbeff106_RelatedTo> syswbeff106_relatedtos;




    private syswbeff106_RelatedTo syswbeff106_relatedto;


    public syswbeff106_Thing(
        int id    ) {
        this.id = id;
        this.syswbeff106_relatedtos = new ArrayList<>();
    }

    public syswbeff106_Thing(
        int id        ArrayList<syswbeff106_RelatedTo> syswbeff106_relatedtos    ) {
        this.id = id;
        this.syswbeff106_relatedtos = syswbeff106_relatedtos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public syswbeff106_RelatedTo getSyswbeff106_relatedto() {
        return syswbeff106_relatedto;
    }

    public void setSyswbeff106_relatedto(syswbeff106_RelatedTo syswbeff106_relatedto) {
        this.syswbeff106_relatedto = syswbeff106_relatedto;
    }
    public List<syswbeff106_RelatedTo> getSyswbeff106_relatedtos() {
        return syswbeff106_relatedtos;
    }

    public void addSyswbeff106_relatedto(Syswbeff106_relatedto syswbeff106_relatedto) {
        this.syswbeff106_relatedtos.add(syswbeff106_relatedto);
    }
    public syswbeff106_RelatedTo getSyswbeff106_relatedto() {
        return syswbeff106_relatedto;
    }

    public void setSyswbeff106_relatedto(syswbeff106_RelatedTo syswbeff106_relatedto) {
        this.syswbeff106_relatedto = syswbeff106_relatedto;
    }

}