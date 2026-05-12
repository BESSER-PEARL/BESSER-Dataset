





import java.util.List;
import java.util.ArrayList;

public class Entity  {

    private None properties;
    private None behaviors;





    private List<AbstractProperty> abstractpropertys;


    public Entity(
        None properties,        None behaviors    ) {
        this.properties = properties;
        this.behaviors = behaviors;
        this.abstractpropertys = new ArrayList<>();
    }

    public Entity(
        None properties,        None behaviors        ArrayList<AbstractProperty> abstractpropertys    ) {
        this.properties = properties;
        this.behaviors = behaviors;
        this.abstractpropertys = abstractpropertys;
    }

    public None getProperties() {
        return properties;
    }

    public void setProperties(None properties) {
        this.properties = properties;
    }
    public None getBehaviors() {
        return behaviors;
    }

    public void setBehaviors(None behaviors) {
        this.behaviors = behaviors;
    }

    public List<AbstractProperty> getAbstractpropertys() {
        return abstractpropertys;
    }

    public void addAbstractproperty(Abstractproperty abstractproperty) {
        this.abstractpropertys.add(abstractproperty);
    }

}