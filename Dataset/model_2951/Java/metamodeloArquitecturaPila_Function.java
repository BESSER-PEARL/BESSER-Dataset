





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_Function  {

    private String name;





    private metamodeloArquitecturaPila_Parameter metamodeloarquitecturapila_parameter;




    private metamodeloArquitecturaPila_BusinessLogic metamodeloarquitecturapila_businesslogic;




    private metamodeloArquitecturaPila_Service metamodeloarquitecturapila_service;




    private List<metamodeloArquitecturaPila_Parameter> metamodeloarquitecturapila_parameters;


    public metamodeloArquitecturaPila_Function(
        String name    ) {
        this.name = name;
        this.metamodeloarquitecturapila_parameters = new ArrayList<>();
    }

    public metamodeloArquitecturaPila_Function(
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

    public metamodeloArquitecturaPila_Parameter getMetamodeloarquitecturapila_parameter() {
        return metamodeloarquitecturapila_parameter;
    }

    public void setMetamodeloarquitecturapila_parameter(metamodeloArquitecturaPila_Parameter metamodeloarquitecturapila_parameter) {
        this.metamodeloarquitecturapila_parameter = metamodeloarquitecturapila_parameter;
    }
    public metamodeloArquitecturaPila_BusinessLogic getMetamodeloarquitecturapila_businesslogic() {
        return metamodeloarquitecturapila_businesslogic;
    }

    public void setMetamodeloarquitecturapila_businesslogic(metamodeloArquitecturaPila_BusinessLogic metamodeloarquitecturapila_businesslogic) {
        this.metamodeloarquitecturapila_businesslogic = metamodeloarquitecturapila_businesslogic;
    }
    public metamodeloArquitecturaPila_Service getMetamodeloarquitecturapila_service() {
        return metamodeloarquitecturapila_service;
    }

    public void setMetamodeloarquitecturapila_service(metamodeloArquitecturaPila_Service metamodeloarquitecturapila_service) {
        this.metamodeloarquitecturapila_service = metamodeloarquitecturapila_service;
    }
    public List<metamodeloArquitecturaPila_Parameter> getMetamodeloarquitecturapila_parameters() {
        return metamodeloarquitecturapila_parameters;
    }

    public void addMetamodeloarquitecturapila_parameter(Metamodeloarquitecturapila_parameter metamodeloarquitecturapila_parameter) {
        this.metamodeloarquitecturapila_parameters.add(metamodeloarquitecturapila_parameter);
    }

}