





import java.util.List;
import java.util.ArrayList;

public class webapp_DataStructure extends Named {






    private List<webapp_ServerPage> webapp_serverpages;




    private webapp_ServerPage webapp_serverpage;


    public webapp_DataStructure(
    ) {
        super(
        );
        this.webapp_serverpages = new ArrayList<>();
    }

    public webapp_DataStructure(
        ArrayList<webapp_ServerPage> webapp_serverpages    ) {
        this.webapp_serverpages = webapp_serverpages;
    }


    public List<webapp_ServerPage> getWebapp_serverpages() {
        return webapp_serverpages;
    }

    public void addWebapp_serverpage(Webapp_serverpage webapp_serverpage) {
        this.webapp_serverpages.add(webapp_serverpage);
    }
    public webapp_ServerPage getWebapp_serverpage() {
        return webapp_serverpage;
    }

    public void setWebapp_serverpage(webapp_ServerPage webapp_serverpage) {
        this.webapp_serverpage = webapp_serverpage;
    }

}