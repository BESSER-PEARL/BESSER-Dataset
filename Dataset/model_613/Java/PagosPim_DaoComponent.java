





import java.util.List;
import java.util.ArrayList;

public class PagosPim_DaoComponent extends GenericComponent {






    private PagosPim_DataLayerComponent pagospim_datalayercomponent;




    private PagosPim_Application pagospim_application;


    public PagosPim_DaoComponent(
    ) {
        super(
        );
    }



    public PagosPim_DataLayerComponent getPagospim_datalayercomponent() {
        return pagospim_datalayercomponent;
    }

    public void setPagospim_datalayercomponent(PagosPim_DataLayerComponent pagospim_datalayercomponent) {
        this.pagospim_datalayercomponent = pagospim_datalayercomponent;
    }
    public PagosPim_Application getPagospim_application() {
        return pagospim_application;
    }

    public void setPagospim_application(PagosPim_Application pagospim_application) {
        this.pagospim_application = pagospim_application;
    }

}