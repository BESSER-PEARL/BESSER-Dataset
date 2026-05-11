





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_Entity  {

    private String name;





    private metamodeloArquitecturaPila_Entity metamodeloarquitecturapila_entity;




    private metamodeloArquitecturaPila_BusinessModel metamodeloarquitecturapila_businessmodel;


    public metamodeloArquitecturaPila_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodeloArquitecturaPila_Entity getMetamodeloarquitecturapila_entity() {
        return metamodeloarquitecturapila_entity;
    }

    public void setMetamodeloarquitecturapila_entity(metamodeloArquitecturaPila_Entity metamodeloarquitecturapila_entity) {
        this.metamodeloarquitecturapila_entity = metamodeloarquitecturapila_entity;
    }
    public metamodeloArquitecturaPila_BusinessModel getMetamodeloarquitecturapila_businessmodel() {
        return metamodeloarquitecturapila_businessmodel;
    }

    public void setMetamodeloarquitecturapila_businessmodel(metamodeloArquitecturaPila_BusinessModel metamodeloarquitecturapila_businessmodel) {
        this.metamodeloarquitecturapila_businessmodel = metamodeloarquitecturapila_businessmodel;
    }

}