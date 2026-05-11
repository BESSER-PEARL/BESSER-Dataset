





import java.util.List;
import java.util.ArrayList;

public class frameweb_ResultDependency extends NavigationDependency {

    private String execute;
    private boolean ajax;
    private String render;





    private List<frameweb_Result> frameweb_results;


    public frameweb_ResultDependency(
        String execute,        boolean ajax,        String render    ) {
        super(
        );
        this.execute = execute;
        this.ajax = ajax;
        this.render = render;
        this.frameweb_results = new ArrayList<>();
    }

    public frameweb_ResultDependency(
        String execute,        boolean ajax,        String render        ArrayList<frameweb_Result> frameweb_results    ) {
        this.execute = execute;
        this.ajax = ajax;
        this.render = render;
        this.frameweb_results = frameweb_results;
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
    public String getRender() {
        return render;
    }

    public void setRender(String render) {
        this.render = render;
    }

    public List<frameweb_Result> getFrameweb_results() {
        return frameweb_results;
    }

    public void addFrameweb_result(Frameweb_result frameweb_result) {
        this.frameweb_results.add(frameweb_result);
    }

}