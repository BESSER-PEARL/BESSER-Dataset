





import java.util.List;
import java.util.ArrayList;

public class PagosPim_ViewComponent extends GenericComponent {

    private String title;





    private PagosPim_Application pagospim_application;




    private List<PagosPim_FrontService> pagospim_frontservices;


    public PagosPim_ViewComponent(
        String title    ) {
        super(
        );
        this.title = title;
        this.pagospim_frontservices = new ArrayList<>();
    }

    public PagosPim_ViewComponent(
        String title        ArrayList<PagosPim_FrontService> pagospim_frontservices    ) {
        this.title = title;
        this.pagospim_frontservices = pagospim_frontservices;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public PagosPim_Application getPagospim_application() {
        return pagospim_application;
    }

    public void setPagospim_application(PagosPim_Application pagospim_application) {
        this.pagospim_application = pagospim_application;
    }
    public List<PagosPim_FrontService> getPagospim_frontservices() {
        return pagospim_frontservices;
    }

    public void addPagospim_frontservice(Pagospim_frontservice pagospim_frontservice) {
        this.pagospim_frontservices.add(pagospim_frontservice);
    }

}