





import java.util.List;
import java.util.ArrayList;

public class core_MetamodelModelAnnotation extends Annotation {

    private String metamodel;



    public core_MetamodelModelAnnotation(
        String metamodel    ) {
        super(
        );
        this.metamodel = metamodel;
    }


    public String getMetamodel() {
        return metamodel;
    }

    public void setMetamodel(String metamodel) {
        this.metamodel = metamodel;
    }


}