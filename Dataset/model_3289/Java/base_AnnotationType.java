





import java.util.List;
import java.util.ArrayList;

public class base_AnnotationType  {

    private String targets;
    private String name;





    private base_Annotation base_annotation;




    private base_Documentation base_documentation;




    private List<base_AnnotationAttribute> base_annotationattributes;


    public base_AnnotationType(
        String targets,        String name    ) {
        this.targets = targets;
        this.name = name;
        this.base_annotationattributes = new ArrayList<>();
    }

    public base_AnnotationType(
        String targets,        String name        ArrayList<base_AnnotationAttribute> base_annotationattributes    ) {
        this.targets = targets;
        this.name = name;
        this.base_annotationattributes = base_annotationattributes;
    }

    public String getTargets() {
        return targets;
    }

    public void setTargets(String targets) {
        this.targets = targets;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public base_Annotation getBase_annotation() {
        return base_annotation;
    }

    public void setBase_annotation(base_Annotation base_annotation) {
        this.base_annotation = base_annotation;
    }
    public base_Documentation getBase_documentation() {
        return base_documentation;
    }

    public void setBase_documentation(base_Documentation base_documentation) {
        this.base_documentation = base_documentation;
    }
    public List<base_AnnotationAttribute> getBase_annotationattributes() {
        return base_annotationattributes;
    }

    public void addBase_annotationattribute(Base_annotationattribute base_annotationattribute) {
        this.base_annotationattributes.add(base_annotationattribute);
    }

}