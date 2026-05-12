





import java.util.List;
import java.util.ArrayList;

public class Presenter  {

    private String currentView;
    private String session;



    public Presenter(
        String currentView,        String session    ) {
        this.currentView = currentView;
        this.session = session;
    }


    public String getCurrentview() {
        return currentView;
    }

    public void setCurrentview(String currentView) {
        this.currentView = currentView;
    }
    public String getSession() {
        return session;
    }

    public void setSession(String session) {
        this.session = session;
    }


}