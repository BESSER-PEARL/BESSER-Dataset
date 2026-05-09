





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Part  {

    private boolean smashed;
    private float x;
    private String name;
    private float y;
    private String library;
    private int uid;
    private String technology;
    private int rot;
    private String gate;
    private String device;
    private String deviceset;
    private String value;





    private List<eaglemodel_Variant> eaglemodel_variants;




    private List<eaglemodel_Attribute> eaglemodel_attributes;


    public eaglemodel_Part(
        boolean smashed,        float x,        String name,        float y,        String library,        int uid,        String technology,        int rot,        String gate,        String device,        String deviceset,        String value    ) {
        this.smashed = smashed;
        this.x = x;
        this.name = name;
        this.y = y;
        this.library = library;
        this.uid = uid;
        this.technology = technology;
        this.rot = rot;
        this.gate = gate;
        this.device = device;
        this.deviceset = deviceset;
        this.value = value;
        this.eaglemodel_variants = new ArrayList<>();
        this.eaglemodel_attributes = new ArrayList<>();
    }

    public eaglemodel_Part(
        boolean smashed,        float x,        String name,        float y,        String library,        int uid,        String technology,        int rot,        String gate,        String device,        String deviceset,        String value        ArrayList<eaglemodel_Variant> eaglemodel_variants,        ArrayList<eaglemodel_Attribute> eaglemodel_attributes    ) {
        this.smashed = smashed;
        this.x = x;
        this.name = name;
        this.y = y;
        this.library = library;
        this.uid = uid;
        this.technology = technology;
        this.rot = rot;
        this.gate = gate;
        this.device = device;
        this.deviceset = deviceset;
        this.value = value;
        this.eaglemodel_variants = eaglemodel_variants;
        this.eaglemodel_attributes = eaglemodel_attributes;
    }

    public boolean getSmashed() {
        return smashed;
    }

    public void setSmashed(boolean smashed) {
        this.smashed = smashed;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public String getLibrary() {
        return library;
    }

    public void setLibrary(String library) {
        this.library = library;
    }
    public int getUid() {
        return uid;
    }

    public void setUid(int uid) {
        this.uid = uid;
    }
    public String getTechnology() {
        return technology;
    }

    public void setTechnology(String technology) {
        this.technology = technology;
    }
    public int getRot() {
        return rot;
    }

    public void setRot(int rot) {
        this.rot = rot;
    }
    public String getGate() {
        return gate;
    }

    public void setGate(String gate) {
        this.gate = gate;
    }
    public String getDevice() {
        return device;
    }

    public void setDevice(String device) {
        this.device = device;
    }
    public String getDeviceset() {
        return deviceset;
    }

    public void setDeviceset(String deviceset) {
        this.deviceset = deviceset;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<eaglemodel_Variant> getEaglemodel_variants() {
        return eaglemodel_variants;
    }

    public void addEaglemodel_variant(Eaglemodel_variant eaglemodel_variant) {
        this.eaglemodel_variants.add(eaglemodel_variant);
    }
    public List<eaglemodel_Attribute> getEaglemodel_attributes() {
        return eaglemodel_attributes;
    }

    public void addEaglemodel_attribute(Eaglemodel_attribute eaglemodel_attribute) {
        this.eaglemodel_attributes.add(eaglemodel_attribute);
    }

}