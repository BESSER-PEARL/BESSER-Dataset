





import java.util.List;
import java.util.ArrayList;

public class ryz_Model extends MainComponent {

    private boolean isAbstract;





    private ryz_ModelAssociation ryz_modelassociation;




    private ryz_Model ryz_model;




    private List<ryz_Property> ryz_propertys;




    private ryz_ModelPackage ryz_modelpackage;




    private ryz_ModelAssociation ryz_modelassociation;




    private List<ryz_TableKey> ryz_tablekeys;


    public ryz_Model(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.ryz_propertys = new ArrayList<>();
        this.ryz_tablekeys = new ArrayList<>();
    }

    public ryz_Model(
        boolean isAbstract        ArrayList<ryz_Property> ryz_propertys,        ArrayList<ryz_TableKey> ryz_tablekeys    ) {
        this.isAbstract = isAbstract;
        this.ryz_propertys = ryz_propertys;
        this.ryz_tablekeys = ryz_tablekeys;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public ryz_ModelAssociation getRyz_modelassociation() {
        return ryz_modelassociation;
    }

    public void setRyz_modelassociation(ryz_ModelAssociation ryz_modelassociation) {
        this.ryz_modelassociation = ryz_modelassociation;
    }
    public ryz_Model getRyz_model() {
        return ryz_model;
    }

    public void setRyz_model(ryz_Model ryz_model) {
        this.ryz_model = ryz_model;
    }
    public List<ryz_Property> getRyz_propertys() {
        return ryz_propertys;
    }

    public void addRyz_property(Ryz_property ryz_property) {
        this.ryz_propertys.add(ryz_property);
    }
    public ryz_ModelPackage getRyz_modelpackage() {
        return ryz_modelpackage;
    }

    public void setRyz_modelpackage(ryz_ModelPackage ryz_modelpackage) {
        this.ryz_modelpackage = ryz_modelpackage;
    }
    public ryz_ModelAssociation getRyz_modelassociation() {
        return ryz_modelassociation;
    }

    public void setRyz_modelassociation(ryz_ModelAssociation ryz_modelassociation) {
        this.ryz_modelassociation = ryz_modelassociation;
    }
    public List<ryz_TableKey> getRyz_tablekeys() {
        return ryz_tablekeys;
    }

    public void addRyz_tablekey(Ryz_tablekey ryz_tablekey) {
        this.ryz_tablekeys.add(ryz_tablekey);
    }

}