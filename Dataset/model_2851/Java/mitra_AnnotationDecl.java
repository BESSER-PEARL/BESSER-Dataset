





import java.util.List;
import java.util.ArrayList;

public class mitra_AnnotationDecl  {

    private String name;
    private boolean required;
    private String targets;
    private boolean many;





    private mitra_Literal mitra_literal;




    private mitra_Annotation mitra_annotation;




    private mitra_PrimitiveType mitra_primitivetype;




    private mitra_AnnotationsDefinition mitra_annotationsdefinition;


    public mitra_AnnotationDecl(
        String name,        boolean required,        String targets,        boolean many    ) {
        this.name = name;
        this.required = required;
        this.targets = targets;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getTargets() {
        return targets;
    }

    public void setTargets(String targets) {
        this.targets = targets;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public mitra_Literal getMitra_literal() {
        return mitra_literal;
    }

    public void setMitra_literal(mitra_Literal mitra_literal) {
        this.mitra_literal = mitra_literal;
    }
    public mitra_Annotation getMitra_annotation() {
        return mitra_annotation;
    }

    public void setMitra_annotation(mitra_Annotation mitra_annotation) {
        this.mitra_annotation = mitra_annotation;
    }
    public mitra_PrimitiveType getMitra_primitivetype() {
        return mitra_primitivetype;
    }

    public void setMitra_primitivetype(mitra_PrimitiveType mitra_primitivetype) {
        this.mitra_primitivetype = mitra_primitivetype;
    }
    public mitra_AnnotationsDefinition getMitra_annotationsdefinition() {
        return mitra_annotationsdefinition;
    }

    public void setMitra_annotationsdefinition(mitra_AnnotationsDefinition mitra_annotationsdefinition) {
        this.mitra_annotationsdefinition = mitra_annotationsdefinition;
    }

}