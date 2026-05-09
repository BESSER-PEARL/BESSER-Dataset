





import java.util.List;
import java.util.ArrayList;

public class domain_MenuFolder extends StyleElement, HTMLLayerHolder, ItemIcon, EnabledUIItem, Categorized, MultiLangLabel {

    private String name;
    private String uid;
    private boolean extensionPoint;



    public domain_MenuFolder(
        String name,        String uid,        boolean extensionPoint    ) {
        super(
        );
        this.name = name;
        this.uid = uid;
        this.extensionPoint = extensionPoint;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public boolean getExtensionpoint() {
        return extensionPoint;
    }

    public void setExtensionpoint(boolean extensionPoint) {
        this.extensionPoint = extensionPoint;
    }


}