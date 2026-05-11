





import java.util.List;
import java.util.ArrayList;

public class viewmodeltrace_Trace  {

    private String state;
    private String traceName;





    private viewmodeltrace_ViewModelTrace viewmodeltrace_viewmodeltrace;


    public viewmodeltrace_Trace(
        String state,        String traceName    ) {
        this.state = state;
        this.traceName = traceName;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getTracename() {
        return traceName;
    }

    public void setTracename(String traceName) {
        this.traceName = traceName;
    }

    public viewmodeltrace_ViewModelTrace getViewmodeltrace_viewmodeltrace() {
        return viewmodeltrace_viewmodeltrace;
    }

    public void setViewmodeltrace_viewmodeltrace(viewmodeltrace_ViewModelTrace viewmodeltrace_viewmodeltrace) {
        this.viewmodeltrace_viewmodeltrace = viewmodeltrace_viewmodeltrace;
    }

}