





import java.util.List;
import java.util.ArrayList;

public class SaveGameWidget  {

    private String okButton;
    private String _listWidget;
    private String cancelButton;



    public SaveGameWidget(
        String okButton,        String _listWidget,        String cancelButton    ) {
        this.okButton = okButton;
        this._listWidget = _listWidget;
        this.cancelButton = cancelButton;
    }


    public String getOkbutton() {
        return okButton;
    }

    public void setOkbutton(String okButton) {
        this.okButton = okButton;
    }
    public String get_listwidget() {
        return _listWidget;
    }

    public void set_listwidget(String _listWidget) {
        this._listWidget = _listWidget;
    }
    public String getCancelbutton() {
        return cancelButton;
    }

    public void setCancelbutton(String cancelButton) {
        this.cancelButton = cancelButton;
    }


}