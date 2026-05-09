





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Instance  {

    private String part;
    private float x;
    private String gate;
    private boolean smashed;
    private float y;
    private int rot;





    private eaglemodel_Instances eaglemodel_instances;




    private List<eaglemodel_Attribute> eaglemodel_attributes;


    public eaglemodel_Instance(
        String part,        float x,        String gate,        boolean smashed,        float y,        int rot    ) {
        this.part = part;
        this.x = x;
        this.gate = gate;
        this.smashed = smashed;
        this.y = y;
        this.rot = rot;
        this.eaglemodel_attributes = new ArrayList<>();
    }

    public eaglemodel_Instance(
        String part,        float x,        String gate,        boolean smashed,        float y,        int rot        ArrayList<eaglemodel_Attribute> eaglemodel_attributes    ) {
        this.part = part;
        this.x = x;
        this.gate = gate;
        this.smashed = smashed;
        this.y = y;
        this.rot = rot;
        this.eaglemodel_attributes = eaglemodel_attributes;
    }

    public String getPart() {
        return part;
    }

    public void setPart(String part) {
        this.part = part;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public String getGate() {
        return gate;
    }

    public void setGate(String gate) {
        this.gate = gate;
    }
    public boolean getSmashed() {
        return smashed;
    }

    public void setSmashed(boolean smashed) {
        this.smashed = smashed;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public int getRot() {
        return rot;
    }

    public void setRot(int rot) {
        this.rot = rot;
    }

    public eaglemodel_Instances getEaglemodel_instances() {
        return eaglemodel_instances;
    }

    public void setEaglemodel_instances(eaglemodel_Instances eaglemodel_instances) {
        this.eaglemodel_instances = eaglemodel_instances;
    }
    public List<eaglemodel_Attribute> getEaglemodel_attributes() {
        return eaglemodel_attributes;
    }

    public void addEaglemodel_attribute(Eaglemodel_attribute eaglemodel_attribute) {
        this.eaglemodel_attributes.add(eaglemodel_attribute);
    }

}