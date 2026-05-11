





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_MenuItem  {

    private String name;
    private String id;





    private metamodeloArquitecturaPila_Menu metamodeloarquitecturapila_menu;




    private metamodeloArquitecturaPila_SimpleComponent metamodeloarquitecturapila_simplecomponent;


    public metamodeloArquitecturaPila_MenuItem(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
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

    public metamodeloArquitecturaPila_Menu getMetamodeloarquitecturapila_menu() {
        return metamodeloarquitecturapila_menu;
    }

    public void setMetamodeloarquitecturapila_menu(metamodeloArquitecturaPila_Menu metamodeloarquitecturapila_menu) {
        this.metamodeloarquitecturapila_menu = metamodeloarquitecturapila_menu;
    }
    public metamodeloArquitecturaPila_SimpleComponent getMetamodeloarquitecturapila_simplecomponent() {
        return metamodeloarquitecturapila_simplecomponent;
    }

    public void setMetamodeloarquitecturapila_simplecomponent(metamodeloArquitecturaPila_SimpleComponent metamodeloarquitecturapila_simplecomponent) {
        this.metamodeloarquitecturapila_simplecomponent = metamodeloarquitecturapila_simplecomponent;
    }

}