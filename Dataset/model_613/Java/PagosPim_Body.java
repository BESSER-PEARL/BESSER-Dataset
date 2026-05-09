





import java.util.List;
import java.util.ArrayList;

public class PagosPim_Body  {






    private PagosPim_ElseSegment pagospim_elsesegment;




    private List<PagosPim_IfBlock> pagospim_ifblocks;




    private PagosPim_Return pagospim_return;




    private PagosPim_Operation pagospim_operation;


    public PagosPim_Body(
    ) {
        this.pagospim_ifblocks = new ArrayList<>();
    }

    public PagosPim_Body(
        ArrayList<PagosPim_IfBlock> pagospim_ifblocks    ) {
        this.pagospim_ifblocks = pagospim_ifblocks;
    }


    public PagosPim_ElseSegment getPagospim_elsesegment() {
        return pagospim_elsesegment;
    }

    public void setPagospim_elsesegment(PagosPim_ElseSegment pagospim_elsesegment) {
        this.pagospim_elsesegment = pagospim_elsesegment;
    }
    public List<PagosPim_IfBlock> getPagospim_ifblocks() {
        return pagospim_ifblocks;
    }

    public void addPagospim_ifblock(Pagospim_ifblock pagospim_ifblock) {
        this.pagospim_ifblocks.add(pagospim_ifblock);
    }
    public PagosPim_Return getPagospim_return() {
        return pagospim_return;
    }

    public void setPagospim_return(PagosPim_Return pagospim_return) {
        this.pagospim_return = pagospim_return;
    }
    public PagosPim_Operation getPagospim_operation() {
        return pagospim_operation;
    }

    public void setPagospim_operation(PagosPim_Operation pagospim_operation) {
        this.pagospim_operation = pagospim_operation;
    }

}