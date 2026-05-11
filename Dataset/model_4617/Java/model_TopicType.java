





import java.util.List;
import java.util.ArrayList;

public class model_TopicType extends TMCLConstruct {

    private String idType;
    private String identifiers;
    private String name;
    private boolean abstract;
    private String kind;
    private String locators;





    private List<model_TopicType> model_topictypes;




    private model_TopicType model_topictype;




    private model_TopicType model_topictype;


    public model_TopicType(
        String idType,        String identifiers,        String name,        boolean abstract,        String kind,        String locators    ) {
        super(
        );
        this.idType = idType;
        this.identifiers = identifiers;
        this.name = name;
        this.abstract = abstract;
        this.kind = kind;
        this.locators = locators;
        this.model_topictypes = new ArrayList<>();
    }

    public model_TopicType(
        String idType,        String identifiers,        String name,        boolean abstract,        String kind,        String locators        ArrayList<model_TopicType> model_topictypes    ) {
        this.idType = idType;
        this.identifiers = identifiers;
        this.name = name;
        this.abstract = abstract;
        this.kind = kind;
        this.locators = locators;
        this.model_topictypes = model_topictypes;
    }

    public String getIdtype() {
        return idType;
    }

    public void setIdtype(String idType) {
        this.idType = idType;
    }
    public String getIdentifiers() {
        return identifiers;
    }

    public void setIdentifiers(String identifiers) {
        this.identifiers = identifiers;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getLocators() {
        return locators;
    }

    public void setLocators(String locators) {
        this.locators = locators;
    }

    public List<model_TopicType> getModel_topictypes() {
        return model_topictypes;
    }

    public void addModel_topictype(Model_topictype model_topictype) {
        this.model_topictypes.add(model_topictype);
    }
    public model_TopicType getModel_topictype() {
        return model_topictype;
    }

    public void setModel_topictype(model_TopicType model_topictype) {
        this.model_topictype = model_topictype;
    }
    public model_TopicType getModel_topictype() {
        return model_topictype;
    }

    public void setModel_topictype(model_TopicType model_topictype) {
        this.model_topictype = model_topictype;
    }

}