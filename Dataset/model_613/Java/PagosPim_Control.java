





import java.util.List;
import java.util.ArrayList;

public class PagosPim_Control  {

    private String label;





    private PagosPim_ViewComponent pagospim_viewcomponent;


    public PagosPim_Control(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public PagosPim_ViewComponent getPagospim_viewcomponent() {
        return pagospim_viewcomponent;
    }

    public void setPagospim_viewcomponent(PagosPim_ViewComponent pagospim_viewcomponent) {
        this.pagospim_viewcomponent = pagospim_viewcomponent;
    }

}