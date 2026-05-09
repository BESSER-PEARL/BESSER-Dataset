





import java.util.List;
import java.util.ArrayList;

public class ASPT_TraceEdge extends TraceElement {

    private String idt;
    private String idsx;
    private String ids;
    private String idtx;



    public ASPT_TraceEdge(
        String idt,        String idsx,        String ids,        String idtx    ) {
        super(
        );
        this.idt = idt;
        this.idsx = idsx;
        this.ids = ids;
        this.idtx = idtx;
    }


    public String getIdt() {
        return idt;
    }

    public void setIdt(String idt) {
        this.idt = idt;
    }
    public String getIdsx() {
        return idsx;
    }

    public void setIdsx(String idsx) {
        this.idsx = idsx;
    }
    public String getIds() {
        return ids;
    }

    public void setIds(String ids) {
        this.ids = ids;
    }
    public String getIdtx() {
        return idtx;
    }

    public void setIdtx(String idtx) {
        this.idtx = idtx;
    }


}