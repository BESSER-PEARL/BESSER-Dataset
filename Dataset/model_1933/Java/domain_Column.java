





import java.util.List;
import java.util.ArrayList;

public class domain_Column extends Orderable, HTMLLayerHolder, StyleElement, Categorized, MultiLangLabel {

    private String uid;
    private String label;



    public domain_Column(
        String uid,        String label    ) {
        super(
        );
        this.uid = uid;
        this.label = label;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}