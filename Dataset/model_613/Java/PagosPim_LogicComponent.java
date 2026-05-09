





import java.util.List;
import java.util.ArrayList;

public class PagosPim_LogicComponent extends GenericComponent {

    private boolean persistible;





    private PagosPim_Application pagospim_application;


    public PagosPim_LogicComponent(
        boolean persistible    ) {
        super(
        );
        this.persistible = persistible;
    }


    public boolean getPersistible() {
        return persistible;
    }

    public void setPersistible(boolean persistible) {
        this.persistible = persistible;
    }

    public PagosPim_Application getPagospim_application() {
        return pagospim_application;
    }

    public void setPagospim_application(PagosPim_Application pagospim_application) {
        this.pagospim_application = pagospim_application;
    }

}