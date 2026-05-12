





import java.util.List;
import java.util.ArrayList;

public class builderState_IReferenceDescription  {

    private int indexInList;
    private String sourceEObjectUri;
    private String containerEObjectURI;
    private String targetEObjectUri;





    private builderState_ResourceDescription builderstate_resourcedescription;


    public builderState_IReferenceDescription(
        int indexInList,        String sourceEObjectUri,        String containerEObjectURI,        String targetEObjectUri    ) {
        this.indexInList = indexInList;
        this.sourceEObjectUri = sourceEObjectUri;
        this.containerEObjectURI = containerEObjectURI;
        this.targetEObjectUri = targetEObjectUri;
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
    public String getContainereobjecturi() {
        return containerEObjectURI;
    }

    public void setContainereobjecturi(String containerEObjectURI) {
        this.containerEObjectURI = containerEObjectURI;
    }
    public String getTargeteobjecturi() {
        return targetEObjectUri;
    }

    public void setTargeteobjecturi(String targetEObjectUri) {
        this.targetEObjectUri = targetEObjectUri;
    }

    public builderState_ResourceDescription getBuilderstate_resourcedescription() {
        return builderstate_resourcedescription;
    }

    public void setBuilderstate_resourcedescription(builderState_ResourceDescription builderstate_resourcedescription) {
        this.builderstate_resourcedescription = builderstate_resourcedescription;
    }

}