





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_Service  {

    private String name;





    private metamodeloArquitecturaPila_Function metamodeloarquitecturapila_function;




    private List<metamodeloArquitecturaPila_Parameter> metamodeloarquitecturapila_parameters;




    private metamodeloArquitecturaPila_Parameter metamodeloarquitecturapila_parameter;




    private metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture;


    public metamodeloArquitecturaPila_Service(
        String name    ) {
        this.name = name;
        this.metamodeloarquitecturapila_parameters = new ArrayList<>();
    }

    public metamodeloArquitecturaPila_Service(
        String name        ArrayList<metamodeloArquitecturaPila_Parameter> metamodeloarquitecturapila_parameters    ) {
        this.name = name;
        this.metamodeloarquitecturapila_parameters = metamodeloarquitecturapila_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodeloArquitecturaPila_Function getMetamodeloarquitecturapila_function() {
        return metamodeloarquitecturapila_function;
    }

    public void setMetamodeloarquitecturapila_function(metamodeloArquitecturaPila_Function metamodeloarquitecturapila_function) {
        this.metamodeloarquitecturapila_function = metamodeloarquitecturapila_function;
    }
    public List<metamodeloArquitecturaPila_Parameter> getMetamodeloarquitecturapila_parameters() {
        return metamodeloarquitecturapila_parameters;
    }

    public void addMetamodeloarquitecturapila_parameter(Metamodeloarquitecturapila_parameter metamodeloarquitecturapila_parameter) {
        this.metamodeloarquitecturapila_parameters.add(metamodeloarquitecturapila_parameter);
    }
    public metamodeloArquitecturaPila_Parameter getMetamodeloarquitecturapila_parameter() {
        return metamodeloarquitecturapila_parameter;
    }

    public void setMetamodeloarquitecturapila_parameter(metamodeloArquitecturaPila_Parameter metamodeloarquitecturapila_parameter) {
        this.metamodeloarquitecturapila_parameter = metamodeloarquitecturapila_parameter;
    }
    public metamodeloArquitecturaPila_Architecture getMetamodeloarquitecturapila_architecture() {
        return metamodeloarquitecturapila_architecture;
    }

    public void setMetamodeloarquitecturapila_architecture(metamodeloArquitecturaPila_Architecture metamodeloarquitecturapila_architecture) {
        this.metamodeloarquitecturapila_architecture = metamodeloarquitecturapila_architecture;
    }

}