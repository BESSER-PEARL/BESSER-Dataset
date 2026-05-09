





import java.util.List;
import java.util.ArrayList;

public class PagosPim_Action extends Control, Operation {






    private PagosPim_FrontService pagospim_frontservice;


    public PagosPim_Action(
    ) {
        super(
        );
    }



    public PagosPim_FrontService getPagospim_frontservice() {
        return pagospim_frontservice;
    }

    public void setPagospim_frontservice(PagosPim_FrontService pagospim_frontservice) {
        this.pagospim_frontservice = pagospim_frontservice;
    }

}