





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_model_ElementoConsulta extends ElementoModelo {

    private String order;





    private model_EADiagram model_eadiagram;


    public gestionmodelosconsultas_model_ElementoConsulta(
        String order    ) {
        super(
        );
        this.order = order;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }

    public model_EADiagram getModel_eadiagram() {
        return model_eadiagram;
    }

    public void setModel_eadiagram(model_EADiagram model_eadiagram) {
        this.model_eadiagram = model_eadiagram;
    }

}