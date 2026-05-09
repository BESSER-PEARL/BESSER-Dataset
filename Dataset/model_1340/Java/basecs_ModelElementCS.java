





import java.util.List;
import java.util.ArrayList;

public class basecs_ModelElementCS extends PivotableElementCS {

    private String csi;
    private String originalXmiId;





    private basecs_AnnotationCS basecs_annotationcs;


    public basecs_ModelElementCS(
        String csi,        String originalXmiId    ) {
        super(
        );
        this.csi = csi;
        this.originalXmiId = originalXmiId;
    }


    public String getCsi() {
        return csi;
    }

    public void setCsi(String csi) {
        this.csi = csi;
    }
    public String getOriginalxmiid() {
        return originalXmiId;
    }

    public void setOriginalxmiid(String originalXmiId) {
        this.originalXmiId = originalXmiId;
    }

    public basecs_AnnotationCS getBasecs_annotationcs() {
        return basecs_annotationcs;
    }

    public void setBasecs_annotationcs(basecs_AnnotationCS basecs_annotationcs) {
        this.basecs_annotationcs = basecs_annotationcs;
    }

}