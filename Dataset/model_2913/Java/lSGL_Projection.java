





import java.util.List;
import java.util.ArrayList;

public class lSGL_Projection  {

    private String name;
    private boolean excluding;





    private List<lSGL_GeneratorAnnotation> lsgl_generatorannotations;




    private List<lSGL_Attribute> lsgl_attributes;




    private lSGL_Model lsgl_model;




    private lSGL_Entity lsgl_entity;


    public lSGL_Projection(
        String name,        boolean excluding    ) {
        this.name = name;
        this.excluding = excluding;
        this.lsgl_generatorannotations = new ArrayList<>();
        this.lsgl_attributes = new ArrayList<>();
    }

    public lSGL_Projection(
        String name,        boolean excluding        ArrayList<lSGL_GeneratorAnnotation> lsgl_generatorannotations,        ArrayList<lSGL_Attribute> lsgl_attributes    ) {
        this.name = name;
        this.excluding = excluding;
        this.lsgl_generatorannotations = lsgl_generatorannotations;
        this.lsgl_attributes = lsgl_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getExcluding() {
        return excluding;
    }

    public void setExcluding(boolean excluding) {
        this.excluding = excluding;
    }

    public List<lSGL_GeneratorAnnotation> getLsgl_generatorannotations() {
        return lsgl_generatorannotations;
    }

    public void addLsgl_generatorannotation(Lsgl_generatorannotation lsgl_generatorannotation) {
        this.lsgl_generatorannotations.add(lsgl_generatorannotation);
    }
    public List<lSGL_Attribute> getLsgl_attributes() {
        return lsgl_attributes;
    }

    public void addLsgl_attribute(Lsgl_attribute lsgl_attribute) {
        this.lsgl_attributes.add(lsgl_attribute);
    }
    public lSGL_Model getLsgl_model() {
        return lsgl_model;
    }

    public void setLsgl_model(lSGL_Model lsgl_model) {
        this.lsgl_model = lsgl_model;
    }
    public lSGL_Entity getLsgl_entity() {
        return lsgl_entity;
    }

    public void setLsgl_entity(lSGL_Entity lsgl_entity) {
        this.lsgl_entity = lsgl_entity;
    }

}