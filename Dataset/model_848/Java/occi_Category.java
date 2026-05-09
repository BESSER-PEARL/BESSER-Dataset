





import java.util.List;
import java.util.ArrayList;

public class occi_Category extends AnnotatedElement {

    private String description;
    private String title;
    private String scheme;
    private String name;
    private String term;





    private List<occi_Attribute> occi_attributes;


    public occi_Category(
        String description,        String title,        String scheme,        String name,        String term    ) {
        super(
        );
        this.description = description;
        this.title = title;
        this.scheme = scheme;
        this.name = name;
        this.term = term;
        this.occi_attributes = new ArrayList<>();
    }

    public occi_Category(
        String description,        String title,        String scheme,        String name,        String term        ArrayList<occi_Attribute> occi_attributes    ) {
        this.description = description;
        this.title = title;
        this.scheme = scheme;
        this.name = name;
        this.term = term;
        this.occi_attributes = occi_attributes;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getScheme() {
        return scheme;
    }

    public void setScheme(String scheme) {
        this.scheme = scheme;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTerm() {
        return term;
    }

    public void setTerm(String term) {
        this.term = term;
    }

    public List<occi_Attribute> getOcci_attributes() {
        return occi_attributes;
    }

    public void addOcci_attribute(Occi_attribute occi_attribute) {
        this.occi_attributes.add(occi_attribute);
    }

}