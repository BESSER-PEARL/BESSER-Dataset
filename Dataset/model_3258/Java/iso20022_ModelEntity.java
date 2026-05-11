





import java.util.List;
import java.util.ArrayList;

public class iso20022_ModelEntity  {

    private String objectIdentifier;





    private List<iso20022_ModelEntity> iso20022_modelentitys;




    private iso20022_ModelEntity iso20022_modelentity;


    public iso20022_ModelEntity(
        String objectIdentifier    ) {
        this.objectIdentifier = objectIdentifier;
        this.iso20022_modelentitys = new ArrayList<>();
    }

    public iso20022_ModelEntity(
        String objectIdentifier        ArrayList<iso20022_ModelEntity> iso20022_modelentitys    ) {
        this.objectIdentifier = objectIdentifier;
        this.iso20022_modelentitys = iso20022_modelentitys;
    }

    public String getObjectidentifier() {
        return objectIdentifier;
    }

    public void setObjectidentifier(String objectIdentifier) {
        this.objectIdentifier = objectIdentifier;
    }

    public List<iso20022_ModelEntity> getIso20022_modelentitys() {
        return iso20022_modelentitys;
    }

    public void addIso20022_modelentity(Iso20022_modelentity iso20022_modelentity) {
        this.iso20022_modelentitys.add(iso20022_modelentity);
    }
    public iso20022_ModelEntity getIso20022_modelentity() {
        return iso20022_modelentity;
    }

    public void setIso20022_modelentity(iso20022_ModelEntity iso20022_modelentity) {
        this.iso20022_modelentity = iso20022_modelentity;
    }

}