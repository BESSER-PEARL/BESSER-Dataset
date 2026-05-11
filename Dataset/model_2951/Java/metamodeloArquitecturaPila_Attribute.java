





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_Attribute  {

    private String name;
    private String value;





    private metamodeloArquitecturaPila_DataType metamodeloarquitecturapila_datatype;




    private metamodeloArquitecturaPila_Entity metamodeloarquitecturapila_entity;


    public metamodeloArquitecturaPila_Attribute(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public metamodeloArquitecturaPila_DataType getMetamodeloarquitecturapila_datatype() {
        return metamodeloarquitecturapila_datatype;
    }

    public void setMetamodeloarquitecturapila_datatype(metamodeloArquitecturaPila_DataType metamodeloarquitecturapila_datatype) {
        this.metamodeloarquitecturapila_datatype = metamodeloarquitecturapila_datatype;
    }
    public metamodeloArquitecturaPila_Entity getMetamodeloarquitecturapila_entity() {
        return metamodeloarquitecturapila_entity;
    }

    public void setMetamodeloarquitecturapila_entity(metamodeloArquitecturaPila_Entity metamodeloarquitecturapila_entity) {
        this.metamodeloarquitecturapila_entity = metamodeloarquitecturapila_entity;
    }

}