





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_View  {

    private String name;





    private metamodeloArquitecturaPila_TitleBar metamodeloarquitecturapila_titlebar;




    private metamodeloArquitecturaPila_Menu metamodeloarquitecturapila_menu;




    private List<metamodeloArquitecturaPila_GraphicalComponent> metamodeloarquitecturapila_graphicalcomponents;




    private List<metamodeloArquitecturaPila_View> metamodeloarquitecturapila_views;




    private metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture;




    private List<metamodeloArquitecturaPila_Form> metamodeloarquitecturapila_forms;


    public metamodeloArquitecturaPila_View(
        String name    ) {
        this.name = name;
        this.metamodeloarquitecturapila_graphicalcomponents = new ArrayList<>();
        this.metamodeloarquitecturapila_views = new ArrayList<>();
        this.metamodeloarquitecturapila_forms = new ArrayList<>();
    }

    public metamodeloArquitecturaPila_View(
        String name        ArrayList<metamodeloArquitecturaPila_GraphicalComponent> metamodeloarquitecturapila_graphicalcomponents,        ArrayList<metamodeloArquitecturaPila_View> metamodeloarquitecturapila_views,        ArrayList<metamodeloArquitecturaPila_Form> metamodeloarquitecturapila_forms    ) {
        this.name = name;
        this.metamodeloarquitecturapila_graphicalcomponents = metamodeloarquitecturapila_graphicalcomponents;
        this.metamodeloarquitecturapila_views = metamodeloarquitecturapila_views;
        this.metamodeloarquitecturapila_forms = metamodeloarquitecturapila_forms;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodeloArquitecturaPila_TitleBar getMetamodeloarquitecturapila_titlebar() {
        return metamodeloarquitecturapila_titlebar;
    }

    public void setMetamodeloarquitecturapila_titlebar(metamodeloArquitecturaPila_TitleBar metamodeloarquitecturapila_titlebar) {
        this.metamodeloarquitecturapila_titlebar = metamodeloarquitecturapila_titlebar;
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
    public List<metamodeloArquitecturaPila_View> getMetamodeloarquitecturapila_views() {
        return metamodeloarquitecturapila_views;
    }

    public void addMetamodeloarquitecturapila_view(Metamodeloarquitecturapila_view metamodeloarquitecturapila_view) {
        this.metamodeloarquitecturapila_views.add(metamodeloarquitecturapila_view);
    }
    public metamodeloArquitecturaPila_Architecture getMetamodeloarquitecturapila_architecture() {
        return metamodeloarquitecturapila_architecture;
    }

    public void setMetamodeloarquitecturapila_architecture(metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture) {
        this.metamodeloarquitecturapila_architecture = metamodeloarquitecturapila_architecture;
    }
    public List<metamodeloArquitecturaPila_Form> getMetamodeloarquitecturapila_forms() {
        return metamodeloarquitecturapila_forms;
    }

    public void addMetamodeloarquitecturapila_form(Metamodeloarquitecturapila_form metamodeloarquitecturapila_form) {
        this.metamodeloarquitecturapila_forms.add(metamodeloarquitecturapila_form);
    }

}