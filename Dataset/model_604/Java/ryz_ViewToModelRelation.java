





import java.util.List;
import java.util.ArrayList;

public class ryz_ViewToModelRelation extends MainComponentRelation {

    private String modelcardinality;





    private ryz_AbstractView ryz_abstractview;




    private ryz_Model ryz_model;




    private List<ryz_Property> ryz_propertys;


    public ryz_ViewToModelRelation(
        String modelcardinality    ) {
        super(
        );
        this.modelcardinality = modelcardinality;
        this.ryz_propertys = new ArrayList<>();
    }

    public ryz_ViewToModelRelation(
        String modelcardinality        ArrayList<ryz_Property> ryz_propertys    ) {
        this.modelcardinality = modelcardinality;
        this.ryz_propertys = ryz_propertys;
    }

    public String getModelcardinality() {
        return modelcardinality;
    }

    public void setModelcardinality(String modelcardinality) {
        this.modelcardinality = modelcardinality;
    }

    public ryz_AbstractView getRyz_abstractview() {
        return ryz_abstractview;
    }

    public void setRyz_abstractview(ryz_AbstractView ryz_abstractview) {
        this.ryz_abstractview = ryz_abstractview;
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

}