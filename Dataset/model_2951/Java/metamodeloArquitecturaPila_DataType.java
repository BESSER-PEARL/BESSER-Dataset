





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_DataType  {

    private String name;





    private metamodeloArquitecturaPila_Parameter metamodeloarquitecturapila_parameter;




    private metamodeloArquitecturaPila_BusinessModel metamodeloarquitecturapila_businessmodel;


    public metamodeloArquitecturaPila_DataType(
        String name    ) {
        this.name = name;
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
    public metamodeloArquitecturaPila_BusinessModel getMetamodeloarquitecturapila_businessmodel() {
        return metamodeloarquitecturapila_businessmodel;
    }

    public void setMetamodeloarquitecturapila_businessmodel(metamodeloArquitecturaPila_BusinessModel metamodeloarquitecturapila_businessmodel) {
        this.metamodeloarquitecturapila_businessmodel = metamodeloarquitecturapila_businessmodel;
    }

}