





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity  {

    private String tipo;
    private String nombreModelElementEntity;





    private RealizacionDiagramEntity realizaciondiagramentity;




    private ModelElementEntity modelelemententity;




    private List<ElementoRealizacionValueAttribute> elementorealizacionvalueattributes;


    public gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity(
        String tipo,        String nombreModelElementEntity    ) {
        this.tipo = tipo;
        this.nombreModelElementEntity = nombreModelElementEntity;
        this.elementorealizacionvalueattributes = new ArrayList<>();
    }

    public gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity(
        String tipo,        String nombreModelElementEntity        ArrayList<ElementoRealizacionValueAttribute> elementorealizacionvalueattributes    ) {
        this.tipo = tipo;
        this.nombreModelElementEntity = nombreModelElementEntity;
        this.elementorealizacionvalueattributes = elementorealizacionvalueattributes;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public String getNombremodelelemententity() {
        return nombreModelElementEntity;
    }

    public void setNombremodelelemententity(String nombreModelElementEntity) {
        this.nombreModelElementEntity = nombreModelElementEntity;
    }

    public RealizacionDiagramEntity getRealizaciondiagramentity() {
        return realizaciondiagramentity;
    }

    public void setRealizaciondiagramentity(RealizacionDiagramEntity realizaciondiagramentity) {
        this.realizaciondiagramentity = realizaciondiagramentity;
    }
    public ModelElementEntity getModelelemententity() {
        return modelelemententity;
    }

    public void setModelelemententity(ModelElementEntity modelelemententity) {
        this.modelelemententity = modelelemententity;
    }
    public List<ElementoRealizacionValueAttribute> getElementorealizacionvalueattributes() {
        return elementorealizacionvalueattributes;
    }

    public void addElementorealizacionvalueattribute(Elementorealizacionvalueattribute elementorealizacionvalueattribute) {
        this.elementorealizacionvalueattributes.add(elementorealizacionvalueattribute);
    }

}