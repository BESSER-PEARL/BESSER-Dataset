





import java.util.List;
import java.util.ArrayList;

public class builderState_IReferenceDescription  {

    private int indexInList;
    private String sourceEObjectUri;
    private String targetEObjectUri;
    private String containerEObjectURI;



    public builderState_IReferenceDescription(
        int indexInList,        String sourceEObjectUri,        String targetEObjectUri,        String containerEObjectURI    ) {
        this.indexInList = indexInList;
        this.sourceEObjectUri = sourceEObjectUri;
        this.targetEObjectUri = targetEObjectUri;
        this.containerEObjectURI = containerEObjectURI;
    }


    public int getIndexinlist() {
        return indexInList;
    }

    public void setIndexinlist(int indexInList) {
        this.indexInList = indexInList;
    }
    public String getSourceeobjecturi() {
        return sourceEObjectUri;
    }

    public void setSourceeobjecturi(String sourceEObjectUri) {
        this.sourceEObjectUri = sourceEObjectUri;
    }
    public String getTargeteobjecturi() {
        return targetEObjectUri;
    }

    public void setTargeteobjecturi(String targetEObjectUri) {
        this.targetEObjectUri = targetEObjectUri;
    }
    public String getContainereobjecturi() {
        return containerEObjectURI;
    }

    public void setContainereobjecturi(String containerEObjectURI) {
        this.containerEObjectURI = containerEObjectURI;
    }


}