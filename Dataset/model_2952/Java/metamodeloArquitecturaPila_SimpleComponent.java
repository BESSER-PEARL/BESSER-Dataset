





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_SimpleComponent extends GraphicalComponent {

    private String value;





    private metamodeloArquitecturaPila_TitleBar metamodeloarquitecturapila_titlebar;


    public metamodeloArquitecturaPila_SimpleComponent(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public metamodeloArquitecturaPila_TitleBar getMetamodeloarquitecturapila_titlebar() {
        return metamodeloarquitecturapila_titlebar;
    }

    public void setMetamodeloarquitecturapila_titlebar(metamodeloArquitecturaPila_TitleBar metamodeloarquitecturapila_titlebar) {
        this.metamodeloarquitecturapila_titlebar = metamodeloarquitecturapila_titlebar;
    }

}