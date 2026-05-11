





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_Service  {

    private String name;





    private metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture;


    public metamodeloArquitecturaPila_Service(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodeloArquitecturaPila_Architecture getMetamodeloarquitecturapila_architecture() {
        return metamodeloarquitecturapila_architecture;
    }

    public void setMetamodeloarquitecturapila_architecture(metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture) {
        this.metamodeloarquitecturapila_architecture = metamodeloarquitecturapila_architecture;
    }

}