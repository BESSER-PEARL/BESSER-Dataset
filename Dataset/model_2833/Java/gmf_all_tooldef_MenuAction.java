





import java.util.List;
import java.util.ArrayList;

public class gmf_all_tooldef_MenuAction extends ContributionItem {

    private String kind;
    private String hotKey;



    public gmf_all_tooldef_MenuAction(
        String kind,        String hotKey    ) {
        super(
        );
        this.kind = kind;
        this.hotKey = hotKey;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getHotkey() {
        return hotKey;
    }

    public void setHotkey(String hotKey) {
        this.hotKey = hotKey;
    }


}