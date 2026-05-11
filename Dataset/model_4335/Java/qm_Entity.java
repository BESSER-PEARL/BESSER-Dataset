





import java.util.List;
import java.util.ArrayList;

public class qm_Entity extends NamedElement {

    private boolean useCase;
    private boolean stakeholder;





    private qm_Entity qm_entity;




    private qm_QualityModel qm_qualitymodel;




    private qm_QualityModel qm_qualitymodel;




    private qm_Entity qm_entity;


    public qm_Entity(
        boolean useCase,        boolean stakeholder    ) {
        super(
        );
        this.useCase = useCase;
        this.stakeholder = stakeholder;
    }


    public boolean getUsecase() {
        return useCase;
    }

    public void setUsecase(boolean useCase) {
        this.useCase = useCase;
    }
    public boolean getStakeholder() {
        return stakeholder;
    }

    public void setStakeholder(boolean stakeholder) {
        this.stakeholder = stakeholder;
    }

    public qm_Entity getQm_entity() {
        return qm_entity;
    }

    public void setQm_entity(qm_Entity qm_entity) {
        this.qm_entity = qm_entity;
    }
    public qm_QualityModel getQm_qualitymodel() {
        return qm_qualitymodel;
    }

    public void setQm_qualitymodel(qm_QualityModel qm_qualitymodel) {
        this.qm_qualitymodel = qm_qualitymodel;
    }
    public qm_QualityModel getQm_qualitymodel() {
        return qm_qualitymodel;
    }

    public void setQm_qualitymodel(qm_QualityModel qm_qualitymodel) {
        this.qm_qualitymodel = qm_qualitymodel;
    }
    public qm_Entity getQm_entity() {
        return qm_entity;
    }

    public void setQm_entity(qm_Entity qm_entity) {
        this.qm_entity = qm_entity;
    }

}