





import java.util.List;
import java.util.ArrayList;

public class model_MAggregationKind  {

    private String name;
    private int kind;





    private model_MAssociation model_massociation;




    private model_MAssociationEnd model_massociationend;


    public model_MAggregationKind(
        String name,        int kind    ) {
        this.name = name;
        this.kind = kind;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getKind() {
        return kind;
    }

    public void setKind(int kind) {
        this.kind = kind;
    }

    public model_MAssociation getModel_massociation() {
        return model_massociation;
    }

    public void setModel_massociation(model_MAssociation model_massociation) {
        this.model_massociation = model_massociation;
    }
    public model_MAssociationEnd getModel_massociationend() {
        return model_massociationend;
    }

    public void setModel_massociationend(model_MAssociationEnd model_massociationend) {
        this.model_massociationend = model_massociationend;
    }

}