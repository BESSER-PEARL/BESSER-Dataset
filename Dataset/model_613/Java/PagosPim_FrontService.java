





import java.util.List;
import java.util.ArrayList;

public class PagosPim_FrontService extends Operation {

    private String fullName;





    private PagosPim_FrontService pagospim_frontservice;




    private PagosPim_ServerService pagospim_serverservice;


    public PagosPim_FrontService(
        String fullName    ) {
        super(
        );
        this.fullName = fullName;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }

    public PagosPim_FrontService getPagospim_frontservice() {
        return pagospim_frontservice;
    }

    public void setPagospim_frontservice(PagosPim_FrontService pagospim_frontservice) {
        this.pagospim_frontservice = pagospim_frontservice;
    }
    public PagosPim_ServerService getPagospim_serverservice() {
        return pagospim_serverservice;
    }

    public void setPagospim_serverservice(PagosPim_ServerService pagospim_serverservice) {
        this.pagospim_serverservice = pagospim_serverservice;
    }

}