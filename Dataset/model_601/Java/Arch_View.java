





import java.util.List;
import java.util.ArrayList;

public class Arch_View  {

    private String name;





    private Arch_FrontEnd arch_frontend;


    public Arch_View(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Arch_FrontEnd getArch_frontend() {
        return arch_frontend;
    }

    public void setArch_frontend(Arch_FrontEnd arch_frontend) {
        this.arch_frontend = arch_frontend;
    }

}