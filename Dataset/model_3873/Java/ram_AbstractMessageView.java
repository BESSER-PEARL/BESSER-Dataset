





import java.util.List;
import java.util.ArrayList;

public class ram_AbstractMessageView  {






    private List<ram_AspectMessageView> ram_aspectmessageviews;




    private ram_Aspect ram_aspect;


    public ram_AbstractMessageView(
    ) {
        this.ram_aspectmessageviews = new ArrayList<>();
    }

    public ram_AbstractMessageView(
        ArrayList<ram_AspectMessageView> ram_aspectmessageviews    ) {
        this.ram_aspectmessageviews = ram_aspectmessageviews;
    }


    public List<ram_AspectMessageView> getRam_aspectmessageviews() {
        return ram_aspectmessageviews;
    }

    public void addRam_aspectmessageview(Ram_aspectmessageview ram_aspectmessageview) {
        this.ram_aspectmessageviews.add(ram_aspectmessageview);
    }
    public ram_Aspect getRam_aspect() {
        return ram_aspect;
    }

    public void setRam_aspect(ram_Aspect ram_aspect) {
        this.ram_aspect = ram_aspect;
    }

}