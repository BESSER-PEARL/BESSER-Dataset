





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_entitymodel_EntityRelation extends ModelElementEntity {

    private String multiplicitySource;
    private String atributteForeingKeySource;
    private String atributtePrimaryKeyTarget;
    private String multiplicityTarget;





    private DiagramEntity diagramentity;


    public gestionmodelosconsultas_entitymodel_EntityRelation(
        String multiplicitySource,        String atributteForeingKeySource,        String atributtePrimaryKeyTarget,        String multiplicityTarget    ) {
        super(
        );
        this.multiplicitySource = multiplicitySource;
        this.atributteForeingKeySource = atributteForeingKeySource;
        this.atributtePrimaryKeyTarget = atributtePrimaryKeyTarget;
        this.multiplicityTarget = multiplicityTarget;
    }


    public String getMultiplicitysource() {
        return multiplicitySource;
    }

    public void setMultiplicitysource(String multiplicitySource) {
        this.multiplicitySource = multiplicitySource;
    }
    public String getAtributteforeingkeysource() {
        return atributteForeingKeySource;
    }

    public void setAtributteforeingkeysource(String atributteForeingKeySource) {
        this.atributteForeingKeySource = atributteForeingKeySource;
    }
    public String getAtributteprimarykeytarget() {
        return atributtePrimaryKeyTarget;
    }

    public void setAtributteprimarykeytarget(String atributtePrimaryKeyTarget) {
        this.atributtePrimaryKeyTarget = atributtePrimaryKeyTarget;
    }
    public String getMultiplicitytarget() {
        return multiplicityTarget;
    }

    public void setMultiplicitytarget(String multiplicityTarget) {
        this.multiplicityTarget = multiplicityTarget;
    }

    public DiagramEntity getDiagramentity() {
        return diagramentity;
    }

    public void setDiagramentity(DiagramEntity diagramentity) {
        this.diagramentity = diagramentity;
    }

}