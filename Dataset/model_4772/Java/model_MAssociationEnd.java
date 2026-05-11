





import java.util.List;
import java.util.ArrayList;

public class model_MAssociationEnd extends MModelElementEx {

    private String mClassName;





    private model_MAssociation model_massociation;




    private model_MAssociation model_massociation;


    public model_MAssociationEnd(
        String mClassName    ) {
        super(
        );
        this.mClassName = mClassName;
    }


    public String getMclassname() {
        return mClassName;
    }

    public void setMclassname(String mClassName) {
        this.mClassName = mClassName;
    }

    public model_MAssociation getModel_massociation() {
        return model_massociation;
    }

    public void setModel_massociation(model_MAssociation model_massociation) {
        this.model_massociation = model_massociation;
    }
    public model_MAssociation getModel_massociation() {
        return model_massociation;
    }

    public void setModel_massociation(model_MAssociation model_massociation) {
        this.model_massociation = model_massociation;
    }

}