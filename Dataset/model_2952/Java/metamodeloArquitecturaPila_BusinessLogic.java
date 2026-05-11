





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_BusinessLogic  {

    private String name;





    private List<metamodeloArquitecturaPila_Function> metamodeloarquitecturapila_functions;




    private metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture;


    public metamodeloArquitecturaPila_BusinessLogic(
        String name    ) {
        this.name = name;
        this.metamodeloarquitecturapila_functions = new ArrayList<>();
    }

    public metamodeloArquitecturaPila_BusinessLogic(
        String name        ArrayList<metamodeloArquitecturaPila_Function> metamodeloarquitecturapila_functions    ) {
        this.name = name;
        this.metamodeloarquitecturapila_functions = metamodeloarquitecturapila_functions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<metamodeloArquitecturaPila_Function> getMetamodeloarquitecturapila_functions() {
        return metamodeloarquitecturapila_functions;
    }

    public void addMetamodeloarquitecturapila_function(Metamodeloarquitecturapila_function metamodeloarquitecturapila_function) {
        this.metamodeloarquitecturapila_functions.add(metamodeloarquitecturapila_function);
    }
    public metamodeloArquitecturaPila_Architecture getMetamodeloarquitecturapila_architecture() {
        return metamodeloarquitecturapila_architecture;
    }

    public void setMetamodeloarquitecturapila_architecture(metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture) {
        this.metamodeloarquitecturapila_architecture = metamodeloarquitecturapila_architecture;
    }

}