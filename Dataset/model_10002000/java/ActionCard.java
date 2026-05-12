





import java.util.List;
import java.util.ArrayList;

public class ActionCard  {

    private String ActionCard_Color_String_;
    private String _attr;
    private String ActionCard__;



    public ActionCard(
        String ActionCard_Color_String_,        String _attr,        String ActionCard__    ) {
        this.ActionCard_Color_String_ = ActionCard_Color_String_;
        this._attr = _attr;
        this.ActionCard__ = ActionCard__;
    }


    public String getActioncard_color_string_() {
        return ActionCard_Color_String_;
    }

    public void setActioncard_color_string_(String ActionCard_Color_String_) {
        this.ActionCard_Color_String_ = ActionCard_Color_String_;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public String getActioncard__() {
        return ActionCard__;
    }

    public void setActioncard__(String ActionCard__) {
        this.ActionCard__ = ActionCard__;
    }


}