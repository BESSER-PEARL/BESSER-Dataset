





import java.util.List;
import java.util.ArrayList;

public class metamodel_ActsAs  {

    private String actsAsWhat;





    private metamodel_Entity metamodel_entity;


    public metamodel_ActsAs(
        String actsAsWhat    ) {
        this.actsAsWhat = actsAsWhat;
    }


    public String getActsaswhat() {
        return actsAsWhat;
    }

    public void setActsaswhat(String actsAsWhat) {
        this.actsAsWhat = actsAsWhat;
    }

    public metamodel_Entity getMetamodel_entity() {
        return metamodel_entity;
    }

    public void setMetamodel_entity(metamodel_Entity metamodel_entity) {
        this.metamodel_entity = metamodel_entity;
    }

}