





import java.util.List;
import java.util.ArrayList;

public class Common_Behavior_Instance extends ModelElement {






    private List<Classifier> classifiers;




    private List<Instance> instances;




    private ComponentInstance componentinstance;




    private List<Link> links;




    private List<LinkEnd> linkends;




    private List<AttributeLink> attributelinks;


    public Common_Behavior_Instance(
    ) {
        super(
        );
        this.classifiers = new ArrayList<>();
        this.instances = new ArrayList<>();
        this.links = new ArrayList<>();
        this.linkends = new ArrayList<>();
        this.attributelinks = new ArrayList<>();
    }

    public Common_Behavior_Instance(
        ArrayList<Classifier> classifiers,        ArrayList<Instance> instances,        ArrayList<Link> links,        ArrayList<LinkEnd> linkends,        ArrayList<AttributeLink> attributelinks    ) {
        this.classifiers = classifiers;
        this.instances = instances;
        this.links = links;
        this.linkends = linkends;
        this.attributelinks = attributelinks;
    }


    public List<Classifier> getClassifiers() {
        return classifiers;
    }

    public void addClassifier(Classifier classifier) {
        this.classifiers.add(classifier);
    }
    public List<Instance> getInstances() {
        return instances;
    }

    public void addInstance(Instance instance) {
        this.instances.add(instance);
    }
    public ComponentInstance getComponentinstance() {
        return componentinstance;
    }

    public void setComponentinstance(ComponentInstance componentinstance) {
        this.componentinstance = componentinstance;
    }
    public List<Link> getLinks() {
        return links;
    }

    public void addLink(Link link) {
        this.links.add(link);
    }
    public List<LinkEnd> getLinkends() {
        return linkends;
    }

    public void addLinkend(Linkend linkend) {
        this.linkends.add(linkend);
    }
    public List<AttributeLink> getAttributelinks() {
        return attributelinks;
    }

    public void addAttributelink(Attributelink attributelink) {
        this.attributelinks.add(attributelink);
    }

}