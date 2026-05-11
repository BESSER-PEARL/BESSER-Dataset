





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_model_Relacion extends ElementoModelo {

    private String order;
    private String estereotipo;





    private model_EADiagram model_eadiagram;


    public gestionmodelosconsultas_model_Relacion(
        String order,        String estereotipo    ) {
        super(
        );
        this.order = order;
        this.estereotipo = estereotipo;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getEstereotipo() {
        return estereotipo;
    }

    public void setEstereotipo(String estereotipo) {
        this.estereotipo = estereotipo;
    }

    public model_EADiagram getModel_eadiagram() {
        return model_eadiagram;
    }

    public void setModel_eadiagram(model_EADiagram model_eadiagram) {
        this.model_eadiagram = model_eadiagram;
    }

}