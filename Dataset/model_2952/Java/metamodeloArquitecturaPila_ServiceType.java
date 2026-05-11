





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_ServiceType  {

    private String name;





    private metamodeloArquitecturaPila_Service metamodeloarquitecturapila_service;




    private metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture;


    public metamodeloArquitecturaPila_ServiceType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodeloArquitecturaPila_Service getMetamodeloarquitecturapila_service() {
        return metamodeloarquitecturapila_service;
    }

    public void setMetamodeloarquitecturapila_service(metamodeloArquitecturaPila_Service metamodeloarquitecturapila_service) {
        this.metamodeloarquitecturapila_service = metamodeloarquitecturapila_service;
    }
    public metamodeloArquitecturaPila_Architecture getMetamodeloarquitecturapila_architecture() {
        return metamodeloarquitecturapila_architecture;
    }

    public void setMetamodeloarquitecturapila_architecture(metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture) {
        this.metamodeloarquitecturapila_architecture = metamodeloarquitecturapila_architecture;
    }

}