





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_BusinessModel  {






    private List<metamodeloArquitecturaPila_Entity> metamodeloarquitecturapila_entitys;




    private metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture;




    private List<metamodeloArquitecturaPila_DataType> metamodeloarquitecturapila_datatypes;


    public metamodeloArquitecturaPila_BusinessModel(
    ) {
        this.metamodeloarquitecturapila_entitys = new ArrayList<>();
        this.metamodeloarquitecturapila_datatypes = new ArrayList<>();
    }

    public metamodeloArquitecturaPila_BusinessModel(
        ArrayList<metamodeloArquitecturaPila_Entity> metamodeloarquitecturapila_entitys,        ArrayList<metamodeloArquitecturaPila_DataType> metamodeloarquitecturapila_datatypes    ) {
        this.metamodeloarquitecturapila_entitys = metamodeloarquitecturapila_entitys;
        this.metamodeloarquitecturapila_datatypes = metamodeloarquitecturapila_datatypes;
    }


    public List<metamodeloArquitecturaPila_Entity> getMetamodeloarquitecturapila_entitys() {
        return metamodeloarquitecturapila_entitys;
    }

    public void addMetamodeloarquitecturapila_entity(Metamodeloarquitecturapila_entity metamodeloarquitecturapila_entity) {
        this.metamodeloarquitecturapila_entitys.add(metamodeloarquitecturapila_entity);
    }
    public metamodeloArquitecturaPila_Architecture getMetamodeloarquitecturapila_architecture() {
        return metamodeloarquitecturapila_architecture;
    }

    public void setMetamodeloarquitecturapila_architecture(metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture) {
        this.metamodeloarquitecturapila_architecture = metamodeloarquitecturapila_architecture;
    }
    public List<metamodeloArquitecturaPila_DataType> getMetamodeloarquitecturapila_datatypes() {
        return metamodeloarquitecturapila_datatypes;
    }

    public void addMetamodeloarquitecturapila_datatype(Metamodeloarquitecturapila_datatype metamodeloarquitecturapila_datatype) {
        this.metamodeloarquitecturapila_datatypes.add(metamodeloarquitecturapila_datatype);
    }

}