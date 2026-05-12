





import java.util.List;
import java.util.ArrayList;

public class build_BuildSet extends ITypedValueContainer {

    private String valueMap;
    private String pathIterator;





    private List<build_PathVector> build_pathvectors;


    public build_BuildSet(
        String valueMap,        String pathIterator    ) {
        super(
        );
        this.valueMap = valueMap;
        this.pathIterator = pathIterator;
        this.build_pathvectors = new ArrayList<>();
    }

    public build_BuildSet(
        String valueMap,        String pathIterator        ArrayList<build_PathVector> build_pathvectors    ) {
        this.valueMap = valueMap;
        this.pathIterator = pathIterator;
        this.build_pathvectors = build_pathvectors;
    }

    public String getValuemap() {
        return valueMap;
    }

    public void setValuemap(String valueMap) {
        this.valueMap = valueMap;
    }
    public String getPathiterator() {
        return pathIterator;
    }

    public void setPathiterator(String pathIterator) {
        this.pathIterator = pathIterator;
    }

    public List<build_PathVector> getBuild_pathvectors() {
        return build_pathvectors;
    }

    public void addBuild_pathvector(Build_pathvector build_pathvector) {
        this.build_pathvectors.add(build_pathvector);
    }

}