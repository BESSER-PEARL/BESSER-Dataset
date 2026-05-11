





import java.util.List;
import java.util.ArrayList;

public class transformation_ExtentMetamodel extends MetamodelDeclaration {

    private boolean generated;



    public transformation_ExtentMetamodel(
        boolean generated    ) {
        super(
        );
        this.generated = generated;
    }


    public boolean getGenerated() {
        return generated;
    }

    public void setGenerated(boolean generated) {
        this.generated = generated;
    }


}