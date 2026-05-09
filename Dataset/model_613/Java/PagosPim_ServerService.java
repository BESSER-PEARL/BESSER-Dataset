





import java.util.List;
import java.util.ArrayList;

public class PagosPim_ServerService extends GenericComponent {






    private PagosPim_Application pagospim_application;




    private PagosPim_LogicComponent pagospim_logiccomponent;


    public PagosPim_ServerService(
    ) {
        super(
        );
    }



    public PagosPim_Application getPagospim_application() {
        return pagospim_application;
    }

    public void setPagospim_application(PagosPim_Application pagospim_application) {
        this.pagospim_application = pagospim_application;
    }
    public PagosPim_LogicComponent getPagospim_logiccomponent() {
        return pagospim_logiccomponent;
    }

    public void setPagospim_logiccomponent(PagosPim_LogicComponent pagospim_logiccomponent) {
        this.pagospim_logiccomponent = pagospim_logiccomponent;
    }

}