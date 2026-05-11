





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_Entity  {

    private String name;





    private List<metamodeloArquitecturaPila_Entity> metamodeloarquitecturapila_entitys;


    public metamodeloArquitecturaPila_Entity(
        String name    ) {
        this.name = name;
        this.metamodeloarquitecturapila_entitys = new ArrayList<>();
    }

    public metamodeloArquitecturaPila_Entity(
        String name        ArrayList<metamodeloArquitecturaPila_Entity> metamodeloarquitecturapila_entitys    ) {
        this.name = name;
        this.metamodeloarquitecturapila_entitys = metamodeloarquitecturapila_entitys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<metamodeloArquitecturaPila_Entity> getMetamodeloarquitecturapila_entitys() {
        return metamodeloarquitecturapila_entitys;
    }

    public void addMetamodeloarquitecturapila_entity(Metamodeloarquitecturapila_entity metamodeloarquitecturapila_entity) {
        this.metamodeloarquitecturapila_entitys.add(metamodeloarquitecturapila_entity);
    }

}