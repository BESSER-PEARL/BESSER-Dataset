





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity  {






    private ElementoRealizacionVisibleAttribute elementorealizacionvisibleattribute;




    private List<ElementoRealizacionDiagramEntity> elementorealizaciondiagramentitys;


    public gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity(
    ) {
        this.elementorealizaciondiagramentitys = new ArrayList<>();
    }

    public gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity(
        ArrayList<ElementoRealizacionDiagramEntity> elementorealizaciondiagramentitys    ) {
        this.elementorealizaciondiagramentitys = elementorealizaciondiagramentitys;
    }


    public ElementoRealizacionVisibleAttribute getElementorealizacionvisibleattribute() {
        return elementorealizacionvisibleattribute;
    }

    public void setElementorealizacionvisibleattribute(ElementoRealizacionVisibleAttribute elementorealizacionvisibleattribute) {
        this.elementorealizacionvisibleattribute = elementorealizacionvisibleattribute;
    }
    public List<ElementoRealizacionDiagramEntity> getElementorealizaciondiagramentitys() {
        return elementorealizaciondiagramentitys;
    }

    public void addElementorealizaciondiagramentity(Elementorealizaciondiagramentity elementorealizaciondiagramentity) {
        this.elementorealizaciondiagramentitys.add(elementorealizaciondiagramentity);
    }

}