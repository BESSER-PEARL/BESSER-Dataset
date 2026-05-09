





import java.util.List;
import java.util.ArrayList;

public class domain_MessageElement extends Uielement, MultiLangLabel {

    private String label;



    public domain_MessageElement(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}