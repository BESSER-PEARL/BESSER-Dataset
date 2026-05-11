





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_View  {

    private String name;





    private List<metamodeloArquitecturaPila_Form> metamodeloarquitecturapila_forms;




    private metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture;




    private metamodeloArquitecturaPila_View metamodeloarquitecturapila_view;




    private metamodeloArquitecturaPila_Menu metamodeloarquitecturapila_menu;




    private List<metamodeloArquitecturaPila_GraphicalComponent> metamodeloarquitecturapila_graphicalcomponents;


    public metamodeloArquitecturaPila_View(
        String name    ) {
        this.name = name;
        this.metamodeloarquitecturapila_forms = new ArrayList<>();
        this.metamodeloarquitecturapila_graphicalcomponents = new ArrayList<>();
    }

    public metamodeloArquitecturaPila_View(
        String name        ArrayList<metamodeloArquitecturaPila_Form> metamodeloarquitecturapila_forms,        ArrayList<metamodeloArquitecturaPila_GraphicalComponent> metamodeloarquitecturapila_graphicalcomponents    ) {
        this.name = name;
        this.metamodeloarquitecturapila_forms = metamodeloarquitecturapila_forms;
        this.metamodeloarquitecturapila_graphicalcomponents = metamodeloarquitecturapila_graphicalcomponents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<metamodeloArquitecturaPila_Form> getMetamodeloarquitecturapila_forms() {
        return metamodeloarquitecturapila_forms;
    }

    public void addMetamodeloarquitecturapila_form(Metamodeloarquitecturapila_form metamodeloarquitecturapila_form) {
        this.metamodeloarquitecturapila_forms.add(metamodeloarquitecturapila_form);
    }
    public metamodeloArquitecturaPila_Architecture getMetamodeloarquitecturapila_architecture() {
        return metamodeloarquitecturapila_architecture;
    }

    public void setMetamodeloarquitecturapila_architecture(metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture) {
        this.metamodeloarquitecturapila_architecture = metamodeloarquitecturapila_architecture;
    }
    public metamodeloArquitecturaPila_View getMetamodeloarquitecturapila_view() {
        return metamodeloarquitecturapila_view;
    }

    public void setMetamodeloarquitecturapila_view(metamodeloArquitecturaPila_View metamodeloarquitecturapila_view) {
        this.metamodeloarquitecturapila_view = metamodeloarquitecturapila_view;
    }
    public metamodeloArquitecturaPila_Menu getMetamodeloarquitecturapila_menu() {
        return metamodeloarquitecturapila_menu;
    }

    public void setMetamodeloarquitecturapila_menu(metamodeloArquitecturaPila_Menu metamodeloarquitecturapila_menu) {
        this.metamodeloarquitecturapila_menu = metamodeloarquitecturapila_menu;
    }
    public List<metamodeloArquitecturaPila_GraphicalComponent> getMetamodeloarquitecturapila_graphicalcomponents() {
        return metamodeloarquitecturapila_graphicalcomponents;
    }

    public void addMetamodeloarquitecturapila_graphicalcomponent(Metamodeloarquitecturapila_graphicalcomponent metamodeloarquitecturapila_graphicalcomponent) {
        this.metamodeloarquitecturapila_graphicalcomponents.add(metamodeloarquitecturapila_graphicalcomponent);
    }

}