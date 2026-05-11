





import java.util.List;
import java.util.ArrayList;

public class hibernate_Entity extends NamedElement {

    private String annotations;





    private hibernate_Package hibernate_package;




    private hibernate_Entity hibernate_entity;




    private List<hibernate_Feature> hibernate_features;




    private hibernate_Reference hibernate_reference;


    public hibernate_Entity(
        String annotations    ) {
        super(
        );
        this.annotations = annotations;
        this.hibernate_features = new ArrayList<>();
    }

    public hibernate_Entity(
        String annotations        ArrayList<hibernate_Feature> hibernate_features    ) {
        this.annotations = annotations;
        this.hibernate_features = hibernate_features;
    }

    public String getAnnotations() {
        return annotations;
    }

    public void setAnnotations(String annotations) {
        this.annotations = annotations;
    }

    public hibernate_Package getHibernate_package() {
        return hibernate_package;
    }

    public void setHibernate_package(hibernate_Package hibernate_package) {
        this.hibernate_package = hibernate_package;
    }
    public hibernate_Entity getHibernate_entity() {
        return hibernate_entity;
    }

    public void setHibernate_entity(hibernate_Entity hibernate_entity) {
        this.hibernate_entity = hibernate_entity;
    }
    public List<hibernate_Feature> getHibernate_features() {
        return hibernate_features;
    }

    public void addHibernate_feature(Hibernate_feature hibernate_feature) {
        this.hibernate_features.add(hibernate_feature);
    }
    public hibernate_Reference getHibernate_reference() {
        return hibernate_reference;
    }

    public void setHibernate_reference(hibernate_Reference hibernate_reference) {
        this.hibernate_reference = hibernate_reference;
    }

}