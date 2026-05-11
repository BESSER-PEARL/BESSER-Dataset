





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_TitleBar  {

    private String name;
    private String id;





    private List<metamodeloArquitecturaPila_SimpleComponent> metamodeloarquitecturapila_simplecomponents;




    private metamodeloArquitecturaPila_View metamodeloarquitecturapila_view;


    public metamodeloArquitecturaPila_TitleBar(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
        this.metamodeloarquitecturapila_simplecomponents = new ArrayList<>();
    }

    public metamodeloArquitecturaPila_TitleBar(
        String name,        String id        ArrayList<metamodeloArquitecturaPila_SimpleComponent> metamodeloarquitecturapila_simplecomponents    ) {
        this.name = name;
        this.id = id;
        this.metamodeloarquitecturapila_simplecomponents = metamodeloarquitecturapila_simplecomponents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<metamodeloArquitecturaPila_SimpleComponent> getMetamodeloarquitecturapila_simplecomponents() {
        return metamodeloarquitecturapila_simplecomponents;
    }

    public void addMetamodeloarquitecturapila_simplecomponent(Metamodeloarquitecturapila_simplecomponent metamodeloarquitecturapila_simplecomponent) {
        this.metamodeloarquitecturapila_simplecomponents.add(metamodeloarquitecturapila_simplecomponent);
    }
    public metamodeloArquitecturaPila_View getMetamodeloarquitecturapila_view() {
        return metamodeloarquitecturapila_view;
    }

    public void setMetamodeloarquitecturapila_view(metamodeloArquitecturaPila_View metamodeloarquitecturapila_view) {
        this.metamodeloarquitecturapila_view = metamodeloarquitecturapila_view;
    }

}