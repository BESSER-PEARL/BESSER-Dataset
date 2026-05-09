





import java.util.List;
import java.util.ArrayList;

public class SMVC_Page  {

    private String title;





    private List<SMVC_Link> smvc_links;




    private SMVC_Controller smvc_controller;




    private SMVC_View smvc_view;


    public SMVC_Page(
        String title    ) {
        this.title = title;
        this.smvc_links = new ArrayList<>();
    }

    public SMVC_Page(
        String title        ArrayList<SMVC_Link> smvc_links    ) {
        this.title = title;
        this.smvc_links = smvc_links;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<SMVC_Link> getSmvc_links() {
        return smvc_links;
    }

    public void addSmvc_link(Smvc_link smvc_link) {
        this.smvc_links.add(smvc_link);
    }
    public SMVC_Controller getSmvc_controller() {
        return smvc_controller;
    }

    public void setSmvc_controller(SMVC_Controller smvc_controller) {
        this.smvc_controller = smvc_controller;
    }
    public SMVC_View getSmvc_view() {
        return smvc_view;
    }

    public void setSmvc_view(SMVC_View smvc_view) {
        this.smvc_view = smvc_view;
    }

}