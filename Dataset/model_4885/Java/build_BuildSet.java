





import java.util.List;
import java.util.ArrayList;

public class build_BuildSet extends ITypedValueContainer {

    private String pathIterator;
    private String valueMap;





    private List<build_PathVector> build_pathvectors;


    public build_BuildSet(
        String pathIterator,        String valueMap    ) {
        super(
        );
        this.pathIterator = pathIterator;
        this.valueMap = valueMap;
        this.build_pathvectors = new ArrayList<>();
    }

    public build_BuildSet(
        String pathIterator,        String valueMap        ArrayList<build_PathVector> build_pathvectors    ) {
        this.pathIterator = pathIterator;
        this.valueMap = valueMap;
        this.build_pathvectors = build_pathvectors;
    }

    public String getPathiterator() {
        return pathIterator;
    }

    public void setPathiterator(String pathIterator) {
        this.pathIterator = pathIterator;
    }
    public String getValuemap() {
        return valueMap;
    }

    public void setValuemap(String valueMap) {
        this.valueMap = valueMap;
    }

    public List<build_PathVector> getBuild_pathvectors() {
        return build_pathvectors;
    }

    public void addBuild_pathvector(Build_pathvector build_pathvector) {
        this.build_pathvectors.add(build_pathvector);
    }

}