





import java.util.List;
import java.util.ArrayList;

public class Arch_Service  {

    private String name;





    private Arch_BackEnd arch_backend;


    public Arch_Service(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Arch_BackEnd getArch_backend() {
        return arch_backend;
    }

    public void setArch_backend(Arch_BackEnd arch_backend) {
        this.arch_backend = arch_backend;
    }

}