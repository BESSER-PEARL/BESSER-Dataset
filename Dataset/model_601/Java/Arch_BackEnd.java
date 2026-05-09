





import java.util.List;
import java.util.ArrayList;

public class Arch_BackEnd  {

    private String name;





    private Arch_Application arch_application;


    public Arch_BackEnd(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Arch_Application getArch_application() {
        return arch_application;
    }

    public void setArch_application(Arch_Application arch_application) {
        this.arch_application = arch_application;
    }

}