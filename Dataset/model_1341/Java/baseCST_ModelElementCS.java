





import java.util.List;
import java.util.ArrayList;

public class baseCST_ModelElementCS extends PivotableElementCS {

    private String originalXmiId;
    private String csi;





    private baseCST_AnnotationCS basecst_annotationcs;


    public baseCST_ModelElementCS(
        String originalXmiId,        String csi    ) {
        super(
        );
        this.originalXmiId = originalXmiId;
        this.csi = csi;
    }


    public String getOriginalxmiid() {
        return originalXmiId;
    }

    public void setOriginalxmiid(String originalXmiId) {
        this.originalXmiId = originalXmiId;
    }
    public String getCsi() {
        return csi;
    }

    public void setCsi(String csi) {
        this.csi = csi;
    }

    public baseCST_AnnotationCS getBasecst_annotationcs() {
        return basecst_annotationcs;
    }

    public void setBasecst_annotationcs(baseCST_AnnotationCS basecst_annotationcs) {
        this.basecst_annotationcs = basecst_annotationcs;
    }

}