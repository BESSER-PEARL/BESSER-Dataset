





import java.util.List;
import java.util.ArrayList;

public class frameweb_ResultDependency extends NavigationDependency {

    private String render;
    private String execute;
    private boolean ajax;



    public frameweb_ResultDependency(
        String render,        String execute,        boolean ajax    ) {
        super(
        );
        this.render = render;
        this.execute = execute;
        this.ajax = ajax;
    }


    public String getRender() {
        return render;
    }

    public void setRender(String render) {
        this.render = render;
    }
    public String getExecute() {
        return execute;
    }

    public void setExecute(String execute) {
        this.execute = execute;
    }
    public boolean getAjax() {
        return ajax;
    }

    public void setAjax(boolean ajax) {
        this.ajax = ajax;
    }


}