





import java.util.List;
import java.util.ArrayList;

public class Arch_Controller  {

    private String name;





    private List<Arch_View> arch_views;




    private Arch_FrontEnd arch_frontend;




    private Arch_View arch_view;


    public Arch_Controller(
        String name    ) {
        this.name = name;
        this.arch_views = new ArrayList<>();
    }

    public Arch_Controller(
        String name        ArrayList<Arch_View> arch_views    ) {
        this.name = name;
        this.arch_views = arch_views;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Arch_View> getArch_views() {
        return arch_views;
    }

    public void addArch_view(Arch_view arch_view) {
        this.arch_views.add(arch_view);
    }
    public Arch_FrontEnd getArch_frontend() {
        return arch_frontend;
    }

    public void setArch_frontend(Arch_FrontEnd arch_frontend) {
        this.arch_frontend = arch_frontend;
    }
    public Arch_View getArch_view() {
        return arch_view;
    }

    public void setArch_view(Arch_View arch_view) {
        this.arch_view = arch_view;
    }

}