





import java.util.List;
import java.util.ArrayList;

public class transformation_CompositeMapping extends ContentMapping {






    private List<transformation_ContentMapping> transformation_contentmappings;


    public transformation_CompositeMapping(
    ) {
        super(
        );
        this.transformation_contentmappings = new ArrayList<>();
    }

    public transformation_CompositeMapping(
        ArrayList<transformation_ContentMapping> transformation_contentmappings    ) {
        this.transformation_contentmappings = transformation_contentmappings;
    }


    public List<transformation_ContentMapping> getTransformation_contentmappings() {
        return transformation_contentmappings;
    }

    public void addTransformation_contentmapping(Transformation_contentmapping transformation_contentmapping) {
        this.transformation_contentmappings.add(transformation_contentmapping);
    }

}