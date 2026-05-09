





import java.util.List;
import java.util.ArrayList;

public class ryz_ViewToControllerRelation extends MainComponentRelation {






    private ryz_ActionMethod ryz_actionmethod;




    private ryz_Model ryz_model;




    private ryz_HelperForSendingRequest ryz_helperforsendingrequest;




    private List<ryz_Property> ryz_propertys;


    public ryz_ViewToControllerRelation(
    ) {
        super(
        );
        this.ryz_propertys = new ArrayList<>();
    }

    public ryz_ViewToControllerRelation(
        ArrayList<ryz_Property> ryz_propertys    ) {
        this.ryz_propertys = ryz_propertys;
    }


    public ryz_ActionMethod getRyz_actionmethod() {
        return ryz_actionmethod;
    }

    public void setRyz_actionmethod(ryz_ActionMethod ryz_actionmethod) {
        this.ryz_actionmethod = ryz_actionmethod;
    }
    public ryz_Model getRyz_model() {
        return ryz_model;
    }

    public void setRyz_model(ryz_Model ryz_model) {
        this.ryz_model = ryz_model;
    }
    public ryz_HelperForSendingRequest getRyz_helperforsendingrequest() {
        return ryz_helperforsendingrequest;
    }

    public void setRyz_helperforsendingrequest(ryz_HelperForSendingRequest ryz_helperforsendingrequest) {
        this.ryz_helperforsendingrequest = ryz_helperforsendingrequest;
    }
    public List<ryz_Property> getRyz_propertys() {
        return ryz_propertys;
    }

    public void addRyz_property(Ryz_property ryz_property) {
        this.ryz_propertys.add(ryz_property);
    }

}