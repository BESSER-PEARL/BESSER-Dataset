





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_GraphicalComponent  {

    private String height;
    private String displayName;
    private String name;
    private String length;
    private String id;





    private metamodeloArquitecturaPila_Form metamodeloarquitecturapila_form;


    public metamodeloArquitecturaPila_GraphicalComponent(
        String height,        String displayName,        String name,        String length,        String id    ) {
        this.height = height;
        this.displayName = displayName;
        this.name = name;
        this.length = length;
        this.id = id;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public metamodeloArquitecturaPila_Form getMetamodeloarquitecturapila_form() {
        return metamodeloarquitecturapila_form;
    }

    public void setMetamodeloarquitecturapila_form(metamodeloArquitecturaPila_Form metamodeloarquitecturapila_form) {
        this.metamodeloarquitecturapila_form = metamodeloarquitecturapila_form;
    }

}